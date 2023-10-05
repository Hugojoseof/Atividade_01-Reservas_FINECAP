
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Reserva
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('listagem')

    else:
        form = ReservaForm()

    return render(request, "core/cadastro.html", {'form': form})

@login_required(login_url='/admin/login/?next=/')
def listagem(request):
    query = request.GET.get("q") if request.GET.get("q") is not None else ""
    data_reserva = request.GET.get("data_reserva") if request.GET.get("data_reserva") is not None else ""
    valor = request.GET.get("valor") if request.GET.get("valor") is not None else ""
    quitado = request.GET.get("quitado")
    print(quitado)

    if request.GET.get("q") is not None:
        reservas = Reserva.objects.filter(
            Q(nome_empresa__icontains=query) &
            Q(data_reserva__contains=data_reserva) &
            Q(stand__valor__icontains=valor)
        )
        if quitado is not None:
            reservas = reservas.filter(quitado=quitado)
    else:
        reservas = Reserva.objects.all()

    paginator = Paginator(reservas, 5)
    print(paginator.num_pages)

    page = request.GET.get('page')
    reservas_pagina = paginator.get_page(page)

    return render(request, 'core/listagem.html', {
        'reservas': reservas_pagina,
        'query': query,
        'valor': valor,
        'data_reserva': data_reserva,
        'quitado': quitado,
    })


def detalhes_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return render(request, 'core/detalhes_reserva.html', {'reserva': reserva})


def excluir_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    reserva.delete()
    return redirect('listagem')

