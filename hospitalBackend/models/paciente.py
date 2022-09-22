from django.db import models
from .usuario import Usuario
from .medico import Medico


class Paciente(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, related_name='paciente', on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, related_name='paciente', on_delete=models.CASCADE)

