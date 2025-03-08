import uuid
from django.shortcuts import redirect, render
from django.http import JsonResponse
import json

from AdminPanel.models import Player
from UserInterface.models import EndUser, Token

# Create your views here.
def UserInfo(request, key=None):
    if request.session.get('token') is None:
        return redirect('logIn')
    
    token = Token.objects.get(token=request.session.get('token'))
    user = token.user
    players = user.players.all()
    total_points = sum([player.get_points() for player in players]) if len(players) == 11 else 0

    context = {
        'user': user,
        'players': players,
        'total_points': f"{total_points:.2f}"
    }

    return render(request, 'UserView.html', context)

def AddPlayertoTeam(request):
    if request.session.get('token') is None:
        return redirect('logIn')

    token = Token.objects.get(token=request.session.get('token'))
    user = token.user

    if request.method == 'POST':
        player_id = request.POST.get('player_id')
        player = Player.objects.get(id=player_id)
        if request.POST.get('add') == '1':
            if user.budget < player.get_value() or user.players.count() == 11:
                return redirect('editTeam')
            if player not in user.players.all():
                user.players.add(player)
                user.budget -= player.get_value()
                user.save()
        else:
            if player in user.players.all():
                user.players.remove(player)
                user.budget += player.get_value()
                user.save()

        teamPlayers = user.players.all()
        for player in teamPlayers:
            player.price = player.get_value()

        filterType = request.GET.get('category')
        print(filterType)
        if filterType is not None:
            otherPlayers = Player.objects.filter(category=filterType).exclude(id__in=[player.id for player in teamPlayers])
        else:
            otherPlayers = Player.objects.exclude(id__in=[player.id for player in teamPlayers])
        
        for player in otherPlayers:
            player.price = player.get_value()

        if len(teamPlayers) == 11:
            total_points = sum([player.get_points() for player in teamPlayers])
        else:
            total_points = 0

        print(teamPlayers)
        context = {
            'players': teamPlayers,
            'availablePlayers': otherPlayers,
            'user': user,
            'total_points': f"{total_points:.2f}"
        }

        return render(request, 'userPlayerView.html', context)

    teamPlayers = user.players.all()
    for player in teamPlayers:
        player.price = player.get_value()

    filterType = request.GET.get('category')
    print(filterType)
    if filterType is not None:
        otherPlayers = Player.objects.filter(category=filterType).exclude(id__in=[player.id for player in teamPlayers])
    else:
        otherPlayers = Player.objects.exclude(id__in=[player.id for player in teamPlayers])
    
    for player in otherPlayers:
        player.price = player.get_value()

    if len(teamPlayers) == 11:
        total_points = sum([player.get_points() for player in teamPlayers])
    else:
        total_points = 0


    context = {
        'players': teamPlayers,
        'availablePlayers': otherPlayers,
        'user': user,
        'total_points': f"{total_points:.2f}"

    }

    return render(request, 'userPlayerView.html', context)


def LogIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin':
            user = EndUser.objects.get(name=username)
            token = Token.objects.update_or_create(user=user, token=str(uuid.uuid4()))
            request.session['token'] = token[0].token
            return redirect('userView')
        else:
            return render(request, 'LogIn.html', {'error': 'Invalid Credentials'})
        
    return render(request, 'LogIn.html')    

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if EndUser.objects.filter(name=username).exists():
            return render(request, 'Register.html', {'error': 'Username already exists'})

        user = EndUser.objects.create(name=username, password=password)
        token = Token.objects.update_or_create(user=user, token=str(uuid.uuid4()))
        request.session['token'] = token[0].token
        return redirect('userView')

    return render(request, 'Register.html')

def LogOut(request):
    request.session.flush()
    return redirect('logIn')

def leaderBoard(request):
    users = EndUser.objects.all()
    for user in users:
        user.points = f"{sum([player.get_points() for player in user.players.all()]):.2f}"
    
    users = sorted(users, key=lambda x: x.points, reverse=True)

    # remove users less than 11 players
    users = [user for user in users if user.players.count() == 11]

    context = {
        'users': users,
        'logged_in_user': Token.objects.get(token=request.session.get('token')).user
    }
    return render(request, 'leaderBoard.html', context)

def userPlayerStatistics(request, player_id):
    player = Player.objects.get(id=player_id)

    player_points = player.get_points()
    player_value = player.get_value()

    context = {
        'player': player,
        'player_points': f'{player_points:.2f}',
        "player_value": player_value

    }
    return render(request, 'userPlayerStatistics.html', context)

def userBudget(request):
    user = Token.objects.get(token=request.session.get('token')).user

    players = user.players.all()
    for player in players:
        player.price = player.get_value()
    
    context = {
        'players': players,
        'user': user,
        'total_spent': sum([player.get_value() for player in players]),
        'remaining': user.budget 
    }

    return render(request, 'budgetView.html', context)