# Generated by Django 3.2.3 on 2021-05-27 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
