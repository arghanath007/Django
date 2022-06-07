# from django.db import models
# import uuid
# from django.contrib.auth.models import User

# # Create your models here.


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email = models.EmailField(max_length=100)
#     username = models.CharField(max_length=100)
#     password =
#     location = models.CharField(max_length=100, null=True, blank=True)
#     social_github = models.CharField(max_length=200, null=True, blank=True)
#     social_twitter = models.CharField(max_length=200, null=True, blank=True)
#     social_linkedin = models.CharField(max_length=200, null=True, blank=True)
#     social_youtube = models.CharField(max_length=200, null=True, blank=True)
#     social_website = models.CharField(max_length=200, null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True,
#                           editable=False, primary_key=True)

#     def __str__(self):
#         return str(self.username)
