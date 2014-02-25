from django import forms
from pocketwingman.models import Result, Category, ResultUser
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class CategoryForm(forms.Form):
    type_of_category = forms.CharField(max_length=200, help_text='Please enter the type of Category')
    created_on = forms.DateTimeField('created on')

    class Meta:
        model = Category



class ResultFormHelpOut(forms.ModelForm):
    category_result = forms.CharField(max_length=200, help_text="Your best line")
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    #created_by = forms.IntegerField(widget=forms.HiddenInput(),initial=2)

    class Meta:
        model = Result
        exclude = ('category','created_by')


class ResultFormHelpMe(forms.ModelForm):
    votes = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Result
        exclude = ('category', 'category_result', 'views','created_by')


class ResultFormHelpMeUser(forms.ModelForm):

    class Meta:
        model = ResultUser
        exclude = ('voted_by', 'category_result', 'down_votes', 'up_votes', 'votes', 'created_on')