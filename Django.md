**Documentation Link** -> https://docs.djangoproject.com/en/4.0/

**Video Link** -> https://www.youtube.com/watch?v=PtQiiknWUcI&t=26s(1hr and 4mins done)

**Course Link** -> Api with Django(Done till part 4)

## To setup a Django Project

1)Create a virtaul environment. Activate the 'venv' and install django in it. Do a pip freeze > requirement.txt, to create a file to keep track of the dependies we need for this project.
2)**django-admin startproject movielist** -> This creates the Django project for us.
3)**python manage.py startapp movielist_app** -> This creates apps which we need with Django.
4)**python manage.py runserver** -> To run the django server locally on the machine.

# MVC

> Model View Controller

# MVT

> Model View Template.
> Django follows the MVT design pattern.

# Django

Django uses the MVT design pattern. The difference from MVC is that Django takes care of the **controller** aspect of things for us.

**Model** -> That the database, that how we model the data. This is the database tables built out in classes.

**Template** -> That's the presentation layer, which the user sees. It is the web page.

**View** -> It is the business logic.

## MVT work-flow/design pattern

> Let's say someone goes to a website(google.com) and they are going through some urls there. Find a url that matches some kind of function in the backend which is the "views" here. The views from the view layer are going to probably grab some data from the "models" and render out some type of "template" to use and we will send that back to the user.

# Commands

## django-admin

> This lists all the core commands that are available in the django-admin.

## django-admin startproject DjangoProject

> This creates a new Django project with the name of 'DjangoProject' here. This is going to create the boilerplate files to setup the django application so it's going to give us the core configuration and basically the basic structure of the project.

## python manage.py runserver

> This is going to run the django development server.

All of the views are going to be handled inside the views.py file from the app(base) that we created.

# Template Inheritance

>

## Templates

> If we create a 'templates' folder in the app(base here) folder, then we have to create a folder with the same name as the app name, so the folder will be called 'base', as the app is called 'base'. With this 'base' folder we can create the templates we want to use for this 'base' app.

## Dynamic URL routing

# Class Based View(CBV)


## Migrations

Command -> **python manage.py migrate**


## Create Super User

> We are creating a super user to test out the Admin Panel.

Command to create a super user -> **python manage.py createsuperuser**


**For MovieList Project**
username -> arghanath
password -> JohnWick@2000


## Converting the Models into SQL queries

Command -> **python manage.py makemigrations**

**This shows that Django supports ORM**. -> We are converting the whole Django code(model) into SQL queries. We use the above command to convert the django code into real database table.

## Register the created model in the admin.py file

>Import the model into the admin.py file and then type the following line to register the model.

**admin.site.register(Movie)**

## Views

1)Class based View
2)Function based View.


### Function based View

def MovieList(request):
    movies=Movie.objects.all() -> Selected all of the data in the form of query set.
    data={
            "movies":list(movies.values()) -> Extracted all of the data, then converted into a list and created a dictionary.
        }
    return JsonResponse(data) -> Converted the dictionary into JSON format with "JsonResponse" and send this dictionary.

> Main motive was to convert queries into Python dictionary and then Python dictionary into JSON response.