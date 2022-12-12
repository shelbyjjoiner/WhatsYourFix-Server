# Generated by Django 4.1.3 on 2022-12-06 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NeuroUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=100)),
                ('hobbies', models.ManyToManyField(to='WhatsYourFixApi.hobbies')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='neuro_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserHobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hobbyists', to='WhatsYourFixApi.hobbies')),
                ('neuro_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WhatsYourFixApi.neurouser')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('item', models.CharField(max_length=25)),
                ('hobbies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hobbie', to='WhatsYourFixApi.hobbies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neuro', to='WhatsYourFixApi.neurouser')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=100)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='WhatsYourFixApi.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='WhatsYourFixApi.neurouser')),
            ],
        ),
    ]
