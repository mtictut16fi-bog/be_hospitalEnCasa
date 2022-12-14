# Generated by Django 4.1.1 on 2022-09-26 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalBackend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='registro',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalBackend.medico'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
