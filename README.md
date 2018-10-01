# Book Lender App
 **Authors**: Ben Hurst
 **Version**: 1.0.0

## Overview

Book Lender App using Django and Psql


## Getting Started

1. Clone or fork repo from github.
2. In a separate terminal instance access the Postgresql terminal by typing ```psql```. Then run ```create database postgres;```.
3. In the terminal, run ```docker-compose up --build```
4. Once the docker container is running, in a separate terminal instance, run ```docker exec -it django_lender_web_1 bash``` and then ```./manage.py createsuperuser```. Then follow the prompts to create an admin.
5. In the browser, go to ```0.0.0.0:8000```

 ## Architecture
Python 3.7, Django Web Framework, Docker, Postgresql
GitHub

 ## API

- **GET** / - the base API route

- **GET** /admin/ - admin console

- **GET** /books/{id} - book list

- **POST** /register/ - 2-factor authentication


 ## Change Log
 09-17-2018 16:50 Basic Scaffolding

 09-18-2018 18:30 Database Populating

 09-19-2018 17:50 Routing works

 09-20-2018 18:50 Styling

 ## License
This project is licensed under the MIT license
