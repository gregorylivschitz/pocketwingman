from django import forms
from pocketwingman.models import Result, Category

class CategoryForm(forms.Form):
    type_of_category = forms.CharField(max_length=200, help_text='Please enter the type of Category')
    created_on = forms.DateTimeField('created on')

    class Meta:
        model = Category



class ResultFormHelpOut(forms.ModelForm):
    category_result = forms.CharField(max_length=200,help_text="Your best line")
    rating = forms.DecimalField(widget=forms.HiddenInput(), initial=0)
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    ratings_count = forms.IntegerField(widget=forms.HiddenInput(),initial=1)
    created_by = forms.IntegerField(widget=forms.HiddenInput(), initial=1)

    class Meta:
        model = Result
        exclude = ('category', 'ratings_count')
        #fields = ('category_result', 'rating', 'votes','category')


class ResultFormHelpMe(forms.ModelForm):
    #category_result = forms.CharField(max_length=200,help_text="Your best line")
    rating = forms.DecimalField(widget=forms.HiddenInput(), initial=0)
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    #ratings_count = forms.IntegerField(widget=forms.HiddenInput(),initial=1)
    created_by = forms.IntegerField(widget=forms.HiddenInput(), initial=1)

    class Meta:
        model = Result
        exclude = ('category', 'category_result')
        #fields = ('category_result', 'rating', 'votes','category')
