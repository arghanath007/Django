p**Django Docs** -> https://docs.djangoproject.com/en/4.0/
**Django REST Framework Docs(DRF)** -> https://www.django-rest-framework.org/

**Video Link** -> https://www.youtube.com/watch?v=PtQiiknWUcI&t=26s(1hr and 4mins done)

**Course Link** -> Views and Serializers(part 3 completed)

## To setup a Django Project

1)Create a virtual environment. Activate the 'venv' and install django in it. Do a pip freeze > requirement.txt, to create a file to keep track of the dependies we need for this project. 2)**django-admin startproject movielist** -> This creates the Django project for us. 3)**python manage.py startapp movielist_app** -> This creates apps which we need with Django. 4)**python manage.py runserver** -> To run the django server locally on the machine.

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


# Function Based View(FBV)

**Steps to create a View(Function Based View)**

1. Create the view.
2. Create the template.
3. Add the URL in the urls.py file

# Class Based View(CBV)

**Steps to create a View(Class Based View)**

1. Create a Model, in models.py file
2. Create the view.
3. Create the template.
4. Add the URL in the urls.py file

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

> Import the model into the admin.py file and then type the following line to register the model.

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

# Django REST Framework(DRF)

> Two concepts in DRF are:

1. Serializations -> Converting the **Complex Datatype**(movies=Movie.objects.all()) into **Python Native Datatype(Python Dictionary)**. After this we have to pass this dictionary in the form of JSON response. If we have to deliver information to the user, we are serializing.

   ### Types of Serializations

   1)ModelSerializer -> **serializers.ModelSerializer**
   2)Serializer -> **serializers.Serializer**

   **serializer=MovieSerializer(movies, many=True)** -> If we have multiple objects, then we have to use the **many=True**.

2. DeSerializations -> When we need to get information from the user and store it in a database, during that part we need to deserialize the data. We get the data in the form of JSON and we convert it into a dictionary and then we have to deserialize it(dictionary) into **Complex Datatype** and store it in the database.

# CRUD Operations

## GET request

> GET request is used to get the data from the database and send/show it to the user. We are going to return the response as the user needs information from the database

## POST request

> If we get POST request which means user is sending some information and we need to store it in the database.

This is for POST request

    def create(self, validated_data):
            return Movie.objects.create(**validated_data)

## PUT request

> If we get PUT request then we are updating all of the fields/columns of that row of data in the database. We rewrite everything.

    def update(self, instance, validated_data):
            instance.name=validated_data.get('name', instance.name)
            instance.description=validated_data.get('description', instance.description)
            instance.active=validated_data.get('active', instance.active)
            instance.save()
            return instance

## PATCH request

> We are partially updating the fields of the data in the database. If we get data for one column then we will update that column of the data in the database.

**def update(self, instance, validated_data):**

instance -> This carries the old values
validated_data -> This carries the new values

# Files

## setting.py

> Main project configuration for the Django project. This is where all the configuration for all the apps that we add, the middlewares. This is where we configure the templates, set up the database and the connection to the database.

## urls.py

> This is the url navigation for the entire app. This is where we determine which routes users go to. These is where we configure how a user navigates the website.

# WSGI -> Web Server Gateway Interface

# ASGI -> Asynchronous Server Gateway Interface

# Apps

## models.py

> Create the database tables

## views.py

> Where the bussiness logic goes, when the functions are triggered when the urls are activated.

## admin.py

> Configure the Admin Panel

## apps.py

> Main app's configuration.

# Templates

### 'DIRS': [

            os.path.join(BASE_DIR, 'templates'),
        ],

> This just lets django know where the templates are. 'BASE_DIR' points to the root directory of the project.

### return render(request, "projects.html")

> Rendering the 'projects.html' template from the templates folder, as we have configured in the setting.py file where to look for the templates.

### {% include 'navbar.html' %}

> To include the navbar.html template into another template.

### {% extends 'main.html' %}

> Extending the 'main.html' template to the 'projects.html' template. So 'main.html' is the parent template and 'projects.html' is the child template.

# Conditionals

{% if number > 10 %}

<p>The number: {{number}} is greater than 10</p>
{% elif number == 10 %}
<p>The number is equal to 10</p>
{% else %}
<p>The number: {{number}} is less than 10</p>
{% endif %}

> This is a conditional statement.

# Database

## python manage.py migrate

> This is used to migrate the database or create tables for the first time.

## To add a new table to the database.

> When we add or update a model field or a model, we have to run the command **python manage.py makemigrations** and then run the command **python manage.py migrate**. To complete the migration.

# Models

> In Django, we model the data using classes.

## models.py

> We are going to create classes that are going to represent tables.

### created=models.DateTimeField(auto_now_add=True)

> Gives the date and time when the data is created. 'auto_now_add=True' means that the date and time will be automatically added when the data is created.

### id=models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

> Overrides the default behaviour of Django and gives the unique id for the data. 'editable=False' means that the id cannot be edited in a form. 'primary_key=True' means that the id is the primary key. We are overriding the default 'id' field given by the Django Model and using uuids instead.

## Database Relationships

### project= models.ForeignKey(Project, on_delete=models.CASCADE)

> Relationship between the two models(Project and Review). 'Project' is the model name where we are creating the relationship. This is a **One to Many** relationship. 'on_delete=models.CASCADE' means that when the 'Project' model is deleted, the 'Review' model will be deleted as well. 'models.SET_NULL' means that the 'Review' model will be left alone and not deleted and the 'project' field will be set to 'Null' when the 'Project' model is deleted.

### tags=models.ManyToManyField('Tag', blank=True)

> Many To Many relationship between Project and Tag Model.

# Admin Panel

### admin.site.register(Project)

> To add the model to the admin page and how this model will be visible in the admin page.

## Django Model Form

> This is used to create a form for the model. It is a way to create a form based on a particular model.

<form method="POST">
  {% csrf_token %} {{form.as_p}}
  <input type="submit" />
</form>

<form method="POST">
  {% csrf_token %}
  {{form.title.label}}
  {{form.title}}
  <input type="submit" />
</form>


> '{% csrf_token %}' this makes sure that the data wasn't manipulated i.e the data is safe and clean. Django automatically creates the form for us. We can use the 'as_p' method which is going to wrap '<p></p>' tags around each field in the form.

    class ProjectForm(ModelForm):
        class Meta:
            model=Project
            field='__add__'

> Creating a form for the Project model. This is a way to create a form based on a particular model. '__all__' means that django is going to generate a field for every available attribute in the 'Project' model.


# Resources

## Django Model Form:

> Link -> https://www.youtube.com/watch?v=VOddmV4Xl1g

enctype="multipart/form-data"

> This is to tell the form that we are going to upload files. Now the form will be able to submit the data(files).

## User Model in Django

> Docs -> https://docs.djangoproject.com/en/4.0/ref/contrib/auth/

## Signals

**def profileUpdated(sender, instance, created, **kwargs):**
    print('Profile Saved')

>Receiver. Function to be triggered. 'sender' is the model that is actually sending the signal. 'instance' is the instance of the model that actually triggered this. 'created' will be a boolean value(True or False) depending on if the user was added or a model was added to the database or the model was simply saved again. It lets us know if a new record was added to the database or not.

**post_save.connect(profileUpdated, sender=Profile)**

>'profileUpdated' is the function we want to trigger. 'sender=Profile' is the model that is sending or triggering the signal. 'post_save' is the signal that is being sent. So anytime 'save' method is called on the Profile model, after the 'save' method is complete, the model is saved. The 'profileUpdated' function will be triggered.



**from django.db.models.signals import post_save, post_delete**

> Importing the Signals

**from django.dispatch import receiver**

> Importing the Decorator of the signals.


**Sending a signal if the Profile was updated or a new Profile was created**

@receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print('Profile Saved')
    print('Sender:', sender)
    print('Instance:', instance)
    print('Created:', created)

> Using Decorators.


def profileUpdated(sender, instance, created, **kwargs):
    print('Profile Saved')
    print('Sender:', sender)
    print('Instance:', instance)
    print('Created:', created)


>Receiver. Function to be triggered. 'sender' is the model that is actually sending the signal. 'instance' is the instance of the model that actually triggered this. 'created' will be a boolean value(True or False) depending on if the user was added or a model was added to the database or the model was simply saved again. It lets us know if a new record was added to the database or not.


post_save.connect(profileUpdated, sender=Profile)

>'profileUpdated' is the function we want to trigger. 'sender=Profile' is the model that is sending or triggering the signal. 'post_save' is the signal that is being sent. So anytime 'save' method is called on the Profile model, after the 'save' method is complete, the model(Profile) is saved. The 'profileUpdated' function will be triggered after the model is saved.



**Deleting a user if the user profile is deleted**

def deleteUser(sender, instance, **kwargs):
    print('Deleting User...')
    print('Sender:', sender)
    print('Instance:', instance)

>In this function, any time we delete a profile, we also want to delete the user.


post_delete.connect(deleteUser, sender=Profile)

>This is triggered whenever a 'Profile' is deleted. So when a 'Profile' is deleted, the user is also deleted.


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    print('Deleting User...')
    print('Sender:', sender)
    print('Instance:', instance)


>Using Decorators.





# Static Files
> They are any kind of css, js, images or any kind of external files that we want to include in the project.

## Add the CSS file in templates

<link rel="stylesheet" href="{% static 'styles/main.css' %}">

> This is how we include the CSS file in the templates.

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

> This is to configure Django where to store the uploaded images. Otherwise Django will store them in the Root Directory and it will be messy. This is simply telling django where to store the uploaded content submitted by the users.

### python manage.py collectstatic

> This commands does is that it collects all the static files from the 'static' folder and the other static files which Django uses and bundles them together into a folder(prodstaticfiles) and then Django takes care from there.


# Production

DEBUG = False 

>In 'DEBUG = False' or in Production mode, Django is looking at 'prodstaticfiles' folder instead of 'staticfiles' which Django was looking at in Development or 'DEBUG = True' mode.

# Pluralize

<span style="font-weight: bold;">{{ project.vote_ratio }}%</span> Positive Feedback ({{ project.vote_total }} Vote{{project.vote_total|pluralize:"s"}})

> 'pluralize' is a filter that is used to pluralize the word. It means that there are multiple votes. '({{ project.vote_total }} Vote{{project.vote_total|pluralize:"s"}})' this means that if the 'vote_total' is more than one(1) then add in the 's' to the word(vote), otherwise just say 'vote'.

# Slice Filter:

{{profile.bio|slice:"150"}}

> This is a filter that is used to slice or for trimming down the text. It means that it will slice the text after the number(150) of characters specified.


# Queries in Django

<div class="dev__skills">
  {% for skill in profile.skill_set.all %}
    <span class="tag tag--pill tag--main">
        <small>{{skill}}</small>
    </span>
  {% endfor %}
</div>


<div class="project__tags">
{% for tag in project.tags.all %}
    <span class="tag tag--pill tag--main">
        <small>{{tag}}</small>
    </span>
{% endfor %}
</div>

> Since Many To Many Relationship

> This is a query that is used to get the skills of the profile of the user. This is how we query a child(skill model) set of objects using the parent model(profile model). '_set.all' means that we are getting all the objects(skills) in the set.


**topSkills = profile.skill_set.exclude(description__exact="")**

> We are getting all the skills from the profile object and excluding the skills that have an empty description. **description__exact=""** means that the description is empty. '_set.exclude' means that we are excluding/not including the skills that have an empty description. Exclude all of the skills that have an empty description and store the rest of them here(topSkills).


**otherSkills = profile.skill_set.filter(description="")**

> This gives us all the values(skills) that have an empty description. '_set.filter' means that we are filtering the skills that have an empty description. Gives us all the skills that have an empty string as the description are stored here(otherSkills).

# Login, Logout User

## Authentication

> Authentication is simply determining who a user is. We are trying to identify a particular user. Login form. Authentication is, who is the user?

## Authorization

> Authorization is simply determining what a user is allowed to do on the website. We are trying to determine if a particular user is allowed to do something. Example, restricting unauthorized users only to a few pages. Some pages will be authorized to logged in users only. Restricting access based on the role of the user in the website like Admin, Manager, Developer, General-User etc.

**user = authenticate(request, username=username, password=password)**

> 'authenticate()' will take the 'username' and the 'password' and it will male sure that the password matches the 'username'. It will return either the 'user' instance or 'None'.


**login(request, user)**

>'login()' create a session for the user in the database.

**logout(request)**


>This is going to delete the session of the logged in user.



**from django.contrib.auth.decorators import login_required**

    @login_required(login_url='login')
    def createProject(request):


> This is a decorator that is used to restrict the access to the page to logged in users only. If the user is not logged in, then it will redirect the user to the login page.


**{% if request.user.is_authenticated %}**


> This is a template tag that is used to check if the user is logged in or not.




# Django Messages FrameWork

**messages.error(request, 'Username or password is incorrect')**

> Sending a flash message to the user


        {% if messages %}
            <ul class="messages">
                {% for message in messages %}
                <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}


> Template to display the flash messages to the user.
            
        


# Starting Tomorrow

# 07 Authentication(video 2)
