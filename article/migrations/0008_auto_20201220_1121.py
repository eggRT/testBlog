# Generated by Django 3.1.4 on 2020-12-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_post_imagepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagePost',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]