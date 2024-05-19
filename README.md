
# Whats-The-Weather web application

### Overview:
Welcome to Whats-The-Weather, a meticulously crafted weather app that levereges cutting-edge technologies. Powered by Flask, Python, CSS and HTML, it delivers a seamless weather experience. It also leverages Gunicorn WSGI server for smooth deployment. Using OpenStreetMap API for maps integration, and OpenMeteo API for weather forecast data.

![app_preview](/docs/AppScreenshot.png)


## Features

-    Current Weather Conditions: Get real-time access to current weather conditions, including temperature and humidity percentage, at any chosen location.

-    Forecast: Access a 7-day weather forecast for any selected location.

-    Search History: Keep track of previous searches and download forecast data from specific dates and locations.

-    Interactive Map: Visualize search results with an interactive map for each individual search, providing a comprehensive overview of weather conditions.

## Deploy with container

The Whats-The-Weather web application includes a Dockerfile that allows you to build the source files into a Docker image for easy deployment.

### To deploy this project run the following commands:


### build the docker image:
```bash
  docker build -t whatstheweather .
```

### Run a container of the application and expose it on port 80 of the host:
```bash
  docker run -d -p 80:8000 --name webapp whatstheweather
```

## Deploy as a process

make sure you have installed all nececary dependencies:
- python:3.11
- pip
- flask 
- gunicorn 
- requests 
- pandas 
- numpy
- boto3

### Run a process of the application and expose it on port 8000 of the host:
```bash
  gunicorn -w 2 -b 0.0.0.0:8000 app:app
```


