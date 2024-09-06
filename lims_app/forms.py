from django import forms
from django.contrib.auth.models import User
from .models import Users,book

class bookForm(forms.ModelForm):

    name = forms.ModelChoiceField(
        queryset=Users.objects.filter(is_reading=False),
        empty_label="Select a user",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial=1  # Set the default value here (assuming the user with ID 1 is available
    )
    book = forms.ModelChoiceField(
        queryset=book.objects.filter(is_available=True),
        empty_label="Select a book",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial=1  # Set the default value here (assuming the book with ID 1 is available)
    )
    class Meta:
        model = book
        fields = ['name', 'book']