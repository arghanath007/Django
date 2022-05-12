from django.db import models
import uuid


# User model provided by Django to developers.
from django.contrib.auth.models import User


class Profile(models.Model):

    # One to One Relationship. 'on_delete=models.CASCADE' means that if the user is deleted, the profile will be deleted as well.
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    about = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles', default='profiles/user-default.png')

    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return str(self.user.username)


class Skill(models.Model):

    # Connect Skill to a specific user. One to Many Relationship.(Many Skills to One Profile). Profile is the parent model.
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)

    # Name of the Skill
    name = models.CharField(max_length=200, null=True,
                            blank=True)

    # Description of the Skill or what I used the skill for. What did I do with it. What do I know about it.
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return self.name
