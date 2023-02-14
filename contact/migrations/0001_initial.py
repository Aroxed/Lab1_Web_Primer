# Generated by Django 4.1.7 on 2023-02-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='User name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date/Time')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
    ]
