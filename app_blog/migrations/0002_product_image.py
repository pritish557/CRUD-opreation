# Generated by Django 4.0.4 on 2022-05-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]
