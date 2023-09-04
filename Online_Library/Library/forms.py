from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class MemberForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = '__all__'
