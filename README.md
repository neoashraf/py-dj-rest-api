# Django-Practice-App
We eill be building a REST API with Python & Django


# Commands
Run project
docker-compose up

Migrate Command
docker-compose run app python manage.py makemigrations
docker-compose run app python manage.py migrate



# CRUD Coding Steps
-Create model, run migration
-Add the new model to admin
-Create a serializer
-Create viewset or apiview
-Add url for the viewset or apiview