from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SignInForm, UserAuthForm, CharacterForm, BackgroundImageForm, Live_WallpaperForm , MusicTrackForm
# Create your views here.
from .models import BackgroundImage, MusicTrack, Character, Live_Wallpaper

@login_required(login_url='login')
def music_player(request):
    tracks = MusicTrack.objects.all()
    context = {
        'tracks': tracks,
        'user': request.user
    }
    return render(request, 'Summer_APP/music_player.html', context)

def creation_story(request):
    return render(request, 'Summer_APP/creation_story.html')
@login_required(login_url='login')
def characters(request):
    characters = Character.objects.all()
    context = {
        'characters': characters,
        'user': request.user
    }
    return render(request, 'Summer_APP/characters.html', context)
@login_required(login_url='login')
def background_images(request):
    backgrounds = BackgroundImage.objects.all()
    context = {
        'backgrounds': backgrounds,
        'user': request.user
    }
    return render(request, 'Summer_APP/background_images.html', context)

@login_required(login_url='login')
def wallpaper_video(request):
    wallpapers = Live_Wallpaper.objects.all()
    context = {
        'wallpapers': wallpapers,
        'user': request.user
    }
    return render(request, 'Summer_APP/wallpaper_video.html', context)

def register(request):  # функция регистрации на сайте
    if request.user.is_authenticated:
        return redirect('profile_page')
    if request.method == 'POST':
        form = UserAuthForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('creation_story')
            # регистрация юзера
    form = UserAuthForm()
    return render(request, 'Summer_APP/register.html', {'form': form})


def login_view(request):  # функция входа на сайте
    if request.user.is_authenticated:
        return redirect('profile_page')
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)  # проверка пароля и логина
            if user is not None:  # проверка найден ли пользователь в бд
                login(request, user)
                return redirect('creation_story')
            else:
                raise ValueError('Пользователь не найден')
                return redirect('login')
    form = SignInForm()
    ctx = {
        'form': form
    }
    return render(request, 'Summer_APP/Login.html', ctx)

def main_content(request):
    ctx = {
        'backgrounds': BackgroundImage.objects.all(),
        'wallpapers': Live_Wallpaper.objects.all(),
        'tracks': MusicTrack.objects.all(),
        'characters': Character.objects.all(),

    }
    return render(request, 'Summer_APP/base.html')

def logout_view(request):
    logout(request)
    return redirect('login')
@staff_member_required(login_url='login')
def add_content(request):
    ctx = {
        'backgrounds': BackgroundImage.objects.all(),
        'wallpapers': Live_Wallpaper.objects.all(),
        'tracks': MusicTrack.objects.all(),
        'characters': Character.objects.all(),
    }
    return render(request, 'Summer_APP/add.html',ctx)

@staff_member_required(login_url='login')
def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('characters')
    ctx = {
        'form': CharacterForm()
    }
    return render(request, 'Summer_APP/characters_create.html',ctx)
@staff_member_required(login_url='login')
def create_background(request):
    if request.method == 'POST':
        form = BackgroundImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('background_images')
    ctx = {
        'form': BackgroundImageForm()
    }
    return render(request, 'Summer_APP/background_create.html',ctx)
@staff_member_required(login_url='login')
def create_music(request):
    if request.method == 'POST':
        form = MusicTrackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music_player')
    ctx = {
        'form': MusicTrackForm()

    }
    return render(request, 'Summer_APP/music_create.html',ctx)

@staff_member_required(login_url='login')
def create_wallpaper(request):
    if request.method == 'POST':
        form = Live_WallpaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('wallpaper_video')
    ctx = {
        'form': Live_WallpaperForm()

    }
    return render(request, 'Summer_APP/wallpaper_create.html',ctx)

# def delete_post_music(request, music_id):
#     post = MusicTrack.objects.get(request, pk=music_id)
#     post.delete()
#     return redirect('music_player')
#
# def delete_post_wallpaper(request, wallpaper_id):
#     post = Live_Wallpaper.objects.get(request, pk=wallpaper_id)
#     post.delete()
#     return redirect('wallpaper_video')
#
# def delete_post_background(request, background_id):
#     post = BackgroundImage.objects.get(request, pk=background_id)
#     post.delete()
#     return redirect('background_images')
#
# def delete_post_character(request, character_id):
#     post = Character.objects.get(request, pk=character_id)
#     post.delete()
#     return redirect('characters')