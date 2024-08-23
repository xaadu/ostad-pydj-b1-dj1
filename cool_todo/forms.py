from django import forms

from .models import Todo


class SearchForm(forms.Form):
    query = forms.CharField()


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
