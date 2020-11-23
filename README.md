# Tinderlike API with Django REST framework

## Done

* Created AppUser Model and Serializer
* Added viewset and routes for AppUser (list, create, retrieve, [...] actions)
* Added tests for AppUser get & create and Potential Matches
* Updated profile picture saving to resize & blur pictures on upload
* Added view and routes to filter potential matches based on parameters (gender, preferred_gender, location)
* Added pagination on the filtered results
* Created Match Model and Serializer for matches between 2 users
* Added a background-task to delete matches older than 14 days every 24h
* Added Swagger UI for API documentation
* Added a GitHub action for CI that checks linting errors and runs tests
* Added docker & docker-compose files
* Added a sample database for testing purposes

## To do

* Update AppUser to take GPS coordinates as location (for now it's a string)
* Update password field to make it secure
* Calculate distance between users based on location coordinates (for now it's checking if the locations are identical)
* Add a view and routes for Matches
* Add tests for Matches
* Document endpoint to list potential matches
* Add support for several preferred genders
* Update background task to run at a specific time every day instead of every 24h

## How to test

### Setup

* Download or clone this repository
* Create an *.env* file with a `SECRET_KEY` value

### Test

#### With docker

* Run `docker-compose run web python manage.py test` to test endpoints
* Run `docker-compose up` to get the app running at http://localhost:8000/

#### Without docker

* Create a python virtual environment and run `pip install -r requirements.txt`
* Run `python manage.py test` to test endpoints
* Run `python manage.py runserver` to get the app running at http://localhost:8000/

API documentation is available at http://localhost:8000/docs
