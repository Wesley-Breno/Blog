# Generated by Django 4.2 on 2023-04-17 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_topo', models.CharField(max_length=32)),
                ('titulo', models.CharField(max_length=50)),
                ('mini_descricao', models.CharField(max_length=120)),
                ('conteudo_post', models.CharField(max_length=500)),
            ],
        ),
    ]
