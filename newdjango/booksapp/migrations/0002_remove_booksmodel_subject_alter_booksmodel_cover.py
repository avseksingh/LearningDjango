# Generated by Django 4.0.2 on 2022-05-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksmodel',
            name='subject',
        ),
        migrations.AlterField(
            model_name='booksmodel',
            name='cover',
            field=models.ImageField(upload_to='static/'),
        ),
    ]