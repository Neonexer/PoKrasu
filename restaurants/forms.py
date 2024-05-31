from django import forms
from django.forms.widgets import Textarea

from restaurants.models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=Textarea(attrs={'placeholder': 'Ваш отзыв:'}))
    class Meta:
        model = Review
        fields = ['text']
