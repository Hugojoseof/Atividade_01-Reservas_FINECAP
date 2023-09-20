import datetime
from django.shortcuts import render,redirect, get_object_or_404
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
    reservas = Reserva.objects.all()
    test = Reserva.objects.filter(stand__valor__gte = 300)

    print(test)
    return render(request, 'core/listagem.html', {'reservas': reservas})

def detalhes_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    return render(request, 'core/detalhes_reserva.html', {'reserva': reserva})

def excluir_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    reserva.delete()
    return redirect('listagem')
