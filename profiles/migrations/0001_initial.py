# Generated by Django 3.2.7 on 2021-09-13 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('user_type', models.IntegerField(choices=[(0, 'Ordinary'), (1, 'SuperHero')], null=True)),
                ('bio', models.CharField(blank=True, max_length=200, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('origin', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]