__author__ = 'devdas'
from django import forms
from rangoapp.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Enter Category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Enter The tile of page")
    url = forms.URLField(max_length=200, help_text="Enter the URL of the page")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        fields = ('title', 'url', 'views')

