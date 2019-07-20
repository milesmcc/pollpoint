# Generated by Django 2.2.3 on 2019-07-20 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SessionUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_connected', models.DateTimeField(auto_now_add=True)),
                ('user_agent', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PollOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poller.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poller.PollOption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poller.SessionUser')),
            ],
        ),
    ]
