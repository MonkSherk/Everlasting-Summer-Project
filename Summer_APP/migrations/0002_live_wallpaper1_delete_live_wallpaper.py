# Generated by Django 4.2.13 on 2024-07-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Summer_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live_Wallpaper1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='video_wallpaper/')),
            ],
        ),
    ]
