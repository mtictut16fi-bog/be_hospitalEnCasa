# Generated by Django 4.1.1 on 2022-09-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalBackend', '0003_alter_medico_especialidad_alter_medico_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]