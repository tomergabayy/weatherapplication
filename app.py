from flask import Flask, render_template, request, send_from_directory
from weather import *
import socket, os

app = Flask(__name__)

BACKGROUND_COLOR = 'blue.jpg'
JSON_FILE_DIR = "/app/history/"

@app.route('/history')
def json_files():
    
    # Get the list of all JSON files in the directory
    json_files = [f for f in os.listdir(JSON_FILE_DIR) if f.endswith('.json')]
    return render_template('history.html', json_files=json_files, background_color=BACKGROUND_COLOR)

@app.route('/download_json/<filename>')
def download_json(filename):
    # Ensure the requested file is within the JSON file directory to prevent directory traversal attacks
    if filename in os.listdir(JSON_FILE_DIR):
        return send_from_directory(JSON_FILE_DIR, filename, as_attachment=True)
    else:
        return "File not found", 404

@app.route('/', methods=['POST', 'GET'])
def results():

    if request.method == 'GET':
        return render_template('index.html', method='get', container=socket.gethostname(), background_color=BACKGROUND_COLOR)

    if request.method == 'POST':

        input_location = request.form.get("place")
        location_data = get_lat_lon(input_location)
        FullPlace = location_data[2]

        form_data = get_forecast(location_data)

        if form_data == "error":
            return render_template('index.html', method='not found', container=socket.gethostname(), background_color=BACKGROUND_COLOR)
        
        create_new_json(form_data,FullPlace)

        current_temp = get_current_temp(location_data)
        return render_template('index.html', form_data=form_data, FullPlace=FullPlace, method='post',current_temp=current_temp, container=socket.gethostname(), lat=location_data[0],lon=location_data[1], background_color=BACKGROUND_COLOR)


if __name__ == "__main__":
    app.run()
