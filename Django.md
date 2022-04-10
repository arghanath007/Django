**Documentation Link** -> https://docs.djangoproject.com/en/4.0/

**Video Link** -> https://www.youtube.com/watch?v=PtQiiknWUcI&t=26s

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
