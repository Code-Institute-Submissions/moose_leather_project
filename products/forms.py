from django import forms
from .models import Item


class ConsignmentForm(forms.ModelForm):
    """Form for registered users to consign items for sale"""

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = '50 character maximum'
        self.fields['description'].widget.attrs['placeholder'] = '200 character maximum'
        self.fields['category'].empty_label = 'Select a Category'
        self.fields['category'].widget.attrs['class'] = 'select-list'

    class Meta:
        model = Item

        labels = {'image': 'Upload Photo --- maximum dimensions are: 400 x 300 pixels and 1 MB max'}
        fields = ('title', 'description', 'price', 'image', 'category')

