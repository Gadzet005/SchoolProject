# Generated by Django 4.0.2 on 2022-02-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_school_description_alter_school_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='sign_password',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Пароль от подписи'),
        ),
        migrations.AddField(
            model_name='schrep',
            name='sign_password',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Пароль от подписи'),
        ),
    ]
