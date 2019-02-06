from django.shortcuts import render
from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator
import datetime
from .models import Consulta

def home(request):
    medicos = Consulta.objects.values('nome_medico').order_by('nome_medico').annotate(Count('nome_medico'))
    return render(request, 'index.html', {
        'medicos' : medicos, 'base_path': request.build_absolute_uri 
    })

def lists(request):
    consultas = Consulta.objects.prefetch_related('exames').annotate(gasto_consulta=Coalesce(Sum('exames__valor_exame'),0)).order_by("gasto_consulta")

    if(request.GET.getlist('nomeMedico')):
        consultas = consultas.filter(nome_medico__in=request.GET.getlist('nomeMedico'))

    if(request.GET.get('de')):
        consultas = consultas.filter(data_consulta__gte=datetime.datetime.strptime(request.GET.get('de'), '%d/%m/%Y').strftime('%Y-%m-%d'))

    if(request.GET.get('ate')):
        consultas = consultas.filter(data_consulta__lte=datetime.datetime.strptime(request.GET.get('ate'), '%d/%m/%Y').strftime('%Y-%m-%d'))
        
    paginator = Paginator(consultas, 10)
    consultas = paginator.page((request.GET.get('page') != "" and request.GET.get('page') or 1))

    return render(request, 'table.html', {
        'consultas' : consultas, 'base_path': request.build_absolute_uri,
    })