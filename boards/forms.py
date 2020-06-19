from django import forms
from django_countries.fields import CountryField
from . import models

class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        board = models.Board.objects.get(pk=pk)
        photo.board = board
        photo.save()
