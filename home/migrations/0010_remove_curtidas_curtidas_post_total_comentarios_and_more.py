# Generated by Django 4.2 on 2023-04-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_curtidas_ip_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curtidas',
            name='curtidas',
        ),
        migrations.AddField(
            model_name='post',
            name='total_comentarios',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='total_curtidas',
            field=models.IntegerField(default=0),
        ),
    ]