# Generated by Django 4.0.6 on 2022-07-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_institucional', '0009_alter_inicio_descricao1_alter_inicio_descricao2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inicio',
            name='titulo1',
            field=models.CharField(max_length=250, verbose_name='Titulo inicial parte 1'),
        ),
        migrations.AlterField(
            model_name='inicio',
            name='titulo2',
            field=models.CharField(max_length=250, verbose_name='Titulo inicial parte 2'),
        ),
    ]
