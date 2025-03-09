from django.shortcuts import redirect, render
from AdminPanel.models import Player
from UserInterface.models import Token


def is_admin(view):
    def wrapper(request, *args, **kwargs):
        if request.session.get('token') is None:
            return redirect('logIn')
        
        token = Token.objects.get(token=request.session.get('token'))
        user = token.user

        if user.type != 'admin':
            return redirect('userView')
        
        return view(request, *args, **kwargs)
    return wrapper

@is_admin
def playerView(request):
    players = Player.objects.all()
    user = Token.objects.get(token=request.session.get('token')).user
    context = {
        'players': players,
        'user': user.type
    }
    return render(request, 'playerView.html', context)

@is_admin
def playerStatistics(request, player_id):
    player = Player.objects.get(id=player_id)

    player_points = player.get_value()
    player_value = player.get_value()

    user = Token.objects.get(token=request.session.get('token')).user

    context = {
        'player': player,
        'player_points': f'{player_points:.2f}',
        "player_value": player_value,
        'user': user.type
    }
    return render(request, 'playerStatistics.html', context)

@is_admin
def tournamentSummery(request):

    players = Player.objects.all()
    total_runs = [(player.id, player.total_runs) for player in players]
    total_wickets = [(player.id ,player.wickets) for player in players]
    highests_runs = max(total_runs, key=lambda x: x[1])
    most_wickets = max(total_wickets, key=lambda x: x[1])

    user = Token.objects.get(token=request.session.get('token')).user

    context = {
        "total_runs": sum([x[1] for x in total_runs]),
        "total_wickets": sum([x[1] for x in total_wickets]),
        "highests_runs": f"{Player.objects.get(id=highests_runs[0]).name} ({highests_runs[1]})",
        "most_wickets": f"{Player.objects.get(id=most_wickets[0]).name} ({most_wickets[1]})",
        'user': user.type
    }

    return render(request, 'tournamentSummery.html', context)

@is_admin
def deletePlayer(request):
    player_id = request.POST.get('player_id')
    player = Player.objects.get(id=player_id)
    player.delete()
    return redirect('playerView')

@is_admin
def updatePlayer(request, player_id):
    player_id = request.POST.get('player_id')
    player = Player.objects.get(id=player_id)

    player.name = request.POST.get('name')
    player.university = request.POST.get('university')
    player.category = request.POST.get('category')
    player.total_runs = request.POST.get('total_runs')
    player.balls_faced = request.POST.get('balls_faced')
    player.innings_played = request.POST.get('innings_played')
    player.wickets = request.POST.get('wickets')
    player.overs_bowled = request.POST.get('overs_bowled')
    player.runs_given = request.POST.get('runs_given')
    player.save()

    return redirect('playerStatistics', player_id=player_id)

@is_admin
def addPlayer(request):

    player_data = {
        'name': request.POST.get('name'),
        'university': request.POST.get('university'),
        'category': request.POST.get('category'),
        'total_runs': request.POST.get('total_runs'),
        'balls_faced': request.POST.get('balls_faced'),
        'innings_played': request.POST.get('innings_played'),
        'wickets': request.POST.get('wickets'),
        'overs_bowled': request.POST.get('overs_bowled'),
        'runs_given': request.POST.get('runs_given')
    }
    
    player = Player(**player_data)
    player.save()

    return redirect('playerStatistics', player_id=player.id)