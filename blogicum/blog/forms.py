# birthday/forms.py
from django import forms

# Импортируем класс модели Birthday.
from .models import Post


class PostForm(forms.ModelForm):
    # Удаляем все описания полей.

    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Post
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        # widgets = {
        #     'birthday': forms.DateInput(attrs={'type': 'date'})
        # } 