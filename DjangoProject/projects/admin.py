from django.contrib import admin
from projects.models import Project, Review, Tag

# Register your models here.


admin.site.register(Project)  # To add the model to the admin page and how this model will be visible in the admin page.
admin.site.register(Review) 
admin.site.register(Tag) 