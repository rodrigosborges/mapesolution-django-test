from django.db import models

class Consulta(models.Model):
    numero_guia_consulta = models.IntegerField(primary_key=True)
    cod_medico = models.IntegerField()
    nome_medico = models.CharField(max_length=255, blank=True, null=True)
    data_consulta = models.DateField(blank=True, null=True)
    valor_consulta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        db_table = 'consulta'

class Exame(models.Model):
    cod_exame = models.IntegerField(primary_key=True)
    numero_guia_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='numero_guia_consulta', related_name='exames')
    valor_exame = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        db_table = 'exame'
        unique_together = (('cod_exame', 'numero_guia_consulta'))