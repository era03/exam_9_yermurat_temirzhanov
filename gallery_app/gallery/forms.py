from django.forms import ValidationError
from gallery.models import Picture
from django import forms


def max_length_validator(string):
    if len(string) > 20:
        raise ValidationError('The max number of characters is 20')
    return string


def min_length_validator(string):
    if len(string) < 8:
        raise ValidationError('The minimum number of characters is 8')
    return


class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ('picture', 'description')