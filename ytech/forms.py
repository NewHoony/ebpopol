from django import forms
from .models import Tech, Book

class TechForm(forms.ModelForm):
    class Meta:
        model = Tech
        fields = ('title','pdf','cover')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        field = ('site_name','site_url','site_con','site_cover')