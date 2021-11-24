# Generated by Django 3.2.2 on 2021-05-21 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_rename_subject_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/user-images-stories/')),
                ('video', models.FileField(blank=True, null=True, upload_to='static/user-videos-stories/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stories', to=settings.AUTH_USER_MODEL)),
                ('views', models.ManyToManyField(blank=True, null=True, related_name='viewers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
