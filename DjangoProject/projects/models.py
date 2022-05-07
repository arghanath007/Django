from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True) # null=True means that the field is optional. 'null' is set to 'false' by default. 'null' is for the database. 'blank' is for the form(django to know). 'blank=True' means that we are allowed to submit a form with description's value being empty when 'filling a form' or doing a 'post' request.
    demo_link= models.CharField(max_length=2000, blank=True, null=True)
    source_link= models.CharField(max_length=2000, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    
    
    
    
    def __str__(self):
        return self.title