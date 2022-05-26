from dataclasses import field
from statistics import mode
from django.forms import ModelForm
from django import forms
from projects.models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link', 'tags']

        widgets = {
            # 'tags' is the field we want to modify. 'forms.CheckboxSelectMultiple()' this turns it into a checkbox field.
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():  # Dictionary
            field.widget.attrs.update({'class': 'input'})

            # self.fields['title'].widget.attrs.update(
            #     {'class': 'input', 'placeholder': 'Add Title'})


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Leave a comment with your vote',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():  # Dictionary
            field.widget.attrs.update({'class': 'input'})
