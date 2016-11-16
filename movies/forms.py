from django import forms
from movies.models import Categories


class Search(forms.Form):
    CHOICES =[('0','all')]
    CHOICES+= Categories.objects.values_list('id','category')
    search= forms.CharField(max_length=64)
    categories=forms.ChoiceField(choices=CHOICES)