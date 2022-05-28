from django.contrib.auth.models import User
from django.core.mail import send_mail


from users.models import Profile
from django.conf import settings


# Create some kind of receive and sender that's going to fire off any time the 'save' method is called on the user 'Profile'.
# This is a signal that fires off after the fact that the user is saved.
from django.db.models.signals import post_save, post_delete

# Decorator
from django.dispatch import receiver


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        # We are automatically connecting the new profile we're creating to the user that triggered it.
        profile = Profile.objects.create(
            user=user, username=user.username, email=user.email, name=user.first_name)

        subject = 'Welcome to DevSearch'
        message = 'Welcome to DevSearch, {}!'.format(user.first_name)

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


post_save.connect(createProfile, sender=User)


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:  # Checking to see if it's not the first instance of the profile.
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


post_save.connect(updateUser, sender=Profile)


def deleteUser(sender, instance, **kwargs):
    # Getting the 'User' of the deleted 'Profile'. 'instance' is the 'Profile' here
    user = instance.user
    user.delete()


# When a Profile is deleted, the user is also deleted.
post_delete.connect(deleteUser, sender=Profile)


# Receiver. Function to be triggered. 'sender' is the model that is actually sending the signal. 'instance' is the instance of the model that actually triggered this. 'created' will be a boolean value(True or False) depending on if the user was added or a model was added to the database or the model was simply saved again. It lets us know if a new record was added to the database or not.

# @receiver(post_save, sender=Profile)
# def profileUpdated(sender, instance, created, **kwargs):
#     print('Profile Saved')
#     print('Sender:', sender)
#     print('Instance:', instance)
#     print('Created:', created)


# 'profileUpdated' is the function we want to trigger. 'sender=Profile' is the model that is sending or triggering the signal. 'post_save' is the signal that is being sent. So anytime 'save' method is called on the Profile model, after the 'save' method is complete, the model(Profile) is saved. The 'profileUpdated' function will be triggered after the model is saved.
# post_save.connect(profileUpdated, sender=Profile)


# In this function, any time we delete a profile, we also want to delete the user.
# def deleteUser(sender, instance, **kwargs):
#     print('Deleting User...')
#     print('Sender:', sender)
#     print('Instance:', instance)


# This is triggered whenever a 'Profile' is deleted. So when a 'Profile' is deleted, the user is also deleted.
# post_delete.connect(deleteUser, sender=Profile)


# Create a signal that creates a user profile any time a user profile is created.


# Fire this function off, whenever a user(User model) is created. 'if created=True' means that the user is being created for the first time. 'instance' is the sender here or instance of the sender.
