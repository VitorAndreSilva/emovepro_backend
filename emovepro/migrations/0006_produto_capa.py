# Generated by Django 5.2 on 2025-04-29 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emovepro', '0005_alter_marca_nome_alter_produto_nome'),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='capa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]
