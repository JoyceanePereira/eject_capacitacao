# Generated by Django 4.0.6 on 2022-07-16 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_institucional', '0008_alter_inicio_descricao1_alter_inicio_descricao2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inicio',
            name='descricao1',
            field=models.TextField(default='', max_length=500, verbose_name='Mensagem de efeito parte 1'),
        ),
        migrations.AlterField(
            model_name='inicio',
            name='descricao2',
            field=models.TextField(default='', max_length=500, verbose_name='Mensagem de efeito parte 2'),
        ),
        migrations.AlterField(
            model_name='inicio',
            name='text_button',
            field=models.CharField(max_length=100, verbose_name='Texto-Botão'),
        ),
    ]
