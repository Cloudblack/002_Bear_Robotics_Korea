# Generated by Django 4.0.4 on 2022-05-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_alter_menu_delete_at_alter_restaurant_delete_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subsidary',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]