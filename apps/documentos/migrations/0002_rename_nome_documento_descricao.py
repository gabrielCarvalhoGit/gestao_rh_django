# Generated by Django 4.2.9 on 2024-01-05 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='nome',
            new_name='descricao',
        ),
    ]
