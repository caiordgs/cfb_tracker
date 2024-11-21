from django.shortcuts import render
from .models import Player, Stat
from .forms import StatForm

def index(request):
    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'players/index.html', context)

def stats(request):
    stats = Stat.objects.all()
    context = {
        'stats': stats,
    }
    return render(request, 'players/stats.html', context)

def add_stat(request):
    if request.method == 'POST':
        form = StatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stats')  # Redireciona para a página de estatísticas
    else:
        form = StatForm()
    return render(request, 'players/add_stat.html', {'form': form})