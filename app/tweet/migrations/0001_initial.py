# Generated by Django 2.2 on 2019-11-20 20:52

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
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Deleted')], default='1', max_length=10)),
                ('content', models.CharField(max_length=160)),
                ('is_retweet', models.BooleanField(default=False)),
                ('is_reply', models.BooleanField(default=False)),
                ('original_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_user', to=settings.AUTH_USER_MODEL)),
                ('tweet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tweet_parent', to='tweet.Tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tweets',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Deleted')], default='1', max_length=10)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.Tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'likes',
            },
        ),
    ]
