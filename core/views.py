
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Reserva
from .forms import ReservaForm
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


def listagem(request):
    query = request.GET.get("q") if request.GET.get("q") is not None else ""
    quitado = request.GET.get("quitado") if request.GET.get("quitado") == 'on' else None
    print(quitado)
    

    if quitado is not None:
        reservas = Reserva.objects.filter(
        Q(nome_empresa__icontains=query)  |
        Q(data_reserva__contains=query) |
        Q(stand__valor__icontains=query) 
    ).filter(
        quitado=bool(quitado)
    )
    else:
        reservas = Reserva.objects.filter(
        Q(nome_empresa__icontains=query)  |
        Q(data_reserva__contains=query) |
        Q(stand__valor__icontains=query) 
    )  

    return render(request, 'core/listagem.html', {'reservas': reservas, 'query': query, "query_quitado": quitado })


def detalhes_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return render(request, 'core/detalhes_reserva.html', {'reserva': reserva})


def excluir_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    reserva.delete()
    return redirect('listagem')
