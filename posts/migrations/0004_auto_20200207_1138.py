# Generated by Django 3.0.3 on 2020-02-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200207_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='imagem',
            field=models.ImageField(upload_to='posts/'),
        ),
    ]