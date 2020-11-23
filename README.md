# Tinderlike API with Django REST framework

## Done

* Created AppUser Model and Serializer
* Added viewset and routes for AppUser (list, create, retrieve, [...] actions)
* Added tests for AppUser get & create
* Updated profile picture saving to resize & blur pictures on upload
* Added view and routes to filter potential matches based on parameters (gender, preferred_gender, location)
* Added pagination on the filtered results
* Created Match Model and Serializer for matches between 2 users
* Added a background-task to delete matches older than 14 days every 24h
* Added Swagger UI for API documentation
* Added a GitHub action for CI that checks linting errors and runs tests

## To do

* Update AppUser to take GPS coordinates as location (for now it's a string)
* Update password field to make it secure
* Calculate distance between users based on location coordinates (for now it's checking if the locations are identical)
* Add a view and routes for Matches
* Add tests for Matches and PotentialMatches
* Document endpoint to list potential matches
* Update background task to run at a specific time every day instead of every 24h
* Add docker & docker-compose files

## How to test

### Setup

* Download or clone this repository
* Create a python virtual environment and run `pip install -r requirements.txt`
* Create an *.env* file with a `SECRET_KEY` value

### Add app users

* Run `python manage.py makemigrations`
* Run `python manage.py migrate`
* Run `python manage.py createsuperuser`
* Run `python manage.py runserver`
* Navigate to [localhost:8000/admin](http://localhost:8000/admin)
* Add several users

### Test

* Run `python manage.py test` to test listing appUsers and creating one
* Navigate to `http://localhost:8000/potentialmatches?gender=female&preferredGender=male&location=<LOCATION\>&email=\<EMAIL\>
to test listing potential matches (with a location and email that you used during the app user creation)

