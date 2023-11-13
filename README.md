# Weather-app
A Weather API based on ```python3.11.4``` and ```FastAPI0.103.0```

## Purpose of the project
The goal of the project was to write the logic for administration and interaction with third-party APIs, in this case with APIs for displaying weather data anywhere in the world

## Main Features
1. User registration
2. User administration
3. Weather data collection

## Installation
Installing dependencies -> You need to install dependencies using the command ```$ pip install -r requirements.txt```

If you do ***NOT*** have pip, follow these [instructions](https://pip.pypa.io/en/stable/installation/)

## Configuration
### All settings for Connecting to databases and APIs are in the src/config.py path:

1. Database settings:  
Connecting to a database, namely PostgreSQL;

2. Token:  
Token for authorization of users and administration (ALGORITHM - hashing algorithm, by default HS256);

3. API keys:  
Keys for connecting to a third-party API for collecting weather data;

4. Redis:  
Connection to redis(For hashing weather data).

## Afterword
I know that it is ***POSSIBLE*** to use the library FastAPI Users([link](https://fastapi-users.github.io/fastapi-users/12.1/)), but I would like to understand the construction and implementation of the registration, authorization and administration logic.
