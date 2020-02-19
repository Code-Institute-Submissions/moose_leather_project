# Generated by Django 3.0.3 on 2020-02-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='images/no_image.png', upload_to='images'),
        ),
    ]
