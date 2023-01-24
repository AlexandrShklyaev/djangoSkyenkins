from django import forms

from category.models import Category, Crib


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'preview']
