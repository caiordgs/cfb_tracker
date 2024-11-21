from django.shortcuts import render, redirect
from .models import Player, Stat, HistoricRecord
from .forms import StatForm

def index(request):
    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'players/index.html', context)

def stats(request):
    stats = Stat.objects.all()
    records = {record.player: record for record in HistoricRecord.objects.all()}

    # Destacar estatísticas que quebram recordes
    for stat in stats:
        stat.breaks_record = {}
        record = records.get(stat.player.name)

        if record:
            # Verificar se as estatísticas atuais superam os recordes
            if stat.passing_yards > record.yards:
                stat.breaks_record["Jardas de Passe"] = True
            if stat.touchdowns_passed > record.touchdowns:
                stat.breaks_record["Touchdowns Passados"] = True
            if stat.rushing_yards > record.rush_yards:
                stat.breaks_record["Jardas Corridas"] = True

            # Adicionar mais comparações para outros recordes conforme necessário
            if stat.passing_completions > record.completions:
                stat.breaks_record["Passes Completos"] = True
            if stat.interceptions < record.interceptions:  # Menos interceptações
                stat.breaks_record["Menos Interceptações"] = True

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
