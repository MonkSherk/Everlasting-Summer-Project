from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  #эти два импорта связанны с юзером в базе данных
from Summer_APP.models import BackgroundImage, MusicTrack, Character, Live_Wallpaper

class UserAuthForm(UserCreationForm):  #форма регистрации
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(forms.Form):  #форма входа
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control' ,
                                                                                 'placeholder': 'Password'}
                                                                            ))

class BackgroundImageForm(forms.ModelForm):
    class Meta:
        model = BackgroundImage
        fields = ['name', 'image']

class MusicTrackForm(forms.ModelForm):
    class Meta:
        model = MusicTrack
        fields = ['title', 'audio_file']

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'description', 'image']

class Live_WallpaperForm(forms.ModelForm):
    class Meta:
        model = Live_Wallpaper
        fields = ['name', 'video']