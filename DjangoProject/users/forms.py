from cProfile import label
from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from users.models import Profile, Skill


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # 'password1' is the first password field. 'password2' is the confirmation password field.
        fields = ['first_name', 'email', 'username',  'password1', 'password2']

        labels = {
            'first_name': 'Full Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():  # Dictionary
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username',
                  'location', 'bio', 'about', 'profile_image', 'social_github', 'social_twitter', 'social_linkedin', 'social_youtube', 'social_website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():  # Dictionary
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        # 'owner' is the field that will not included in the form or excluded from the form.
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():  # Dictionary
            field.widget.attrs.update({'class': 'input'})
