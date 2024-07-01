from django.urls import path
from . import views

urlpatterns = [
    path('', views.creation_story, name='creation_story'),
    # path('character/<int:character_id>/', views.delete_post_character, name='character_delete'),
    # path('background/<int:background_id>/', views.delete_post_background, name='background_delete'),
    # path('music/<int:music_id>/', views.delete_post_music, name='music_delete'),
    # path('wallpaper/<int:wallpaper_id>/', views.delete_post_wallpaper, name='wallpaper_delete'),
    path('create_character', views.create_character, name='create_character'),
    path('create_background', views.create_background, name='create_background'),
    path('create_music', views.create_music, name='create_music'),
    path('create_wallpaper', views.create_wallpaper, name='create_wallpaper'),
    path('add_content', views.add_content, name='add_content'),
    path('wallpaper_video', views.wallpaper_video, name='wallpaper_video'),
    path('characters/', views.characters, name='characters'),
    path('background_images/', views.background_images, name='background_images'),
    path('music_player/', views.music_player, name='music_player'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
