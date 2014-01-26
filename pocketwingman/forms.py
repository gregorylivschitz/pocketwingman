from django import forms
from pocketwingman.models import Result, Category

class CategoryForm(forms.Form):
    type_of_category = forms.CharField(max_length=200, help_text='Please enter the type of Category')
    created_on = forms.DateTimeField('created on')

    class Meta:
        model = Category



class ResultForm(forms.ModelForm):
    category_result = forms.CharField(max_length=200,help_text="Your best line")
    rating = forms.DecimalField(widget=forms.HiddenInput(), initial=0)
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    created_by = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    category = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Result
        fields = ('category_result', 'rating', 'votes')
