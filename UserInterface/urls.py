from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserInfo, name="userView"),
    
    path('login/', views.LogIn, name='logIn'),
    path('logOut/', views.LogOut, name='logOut'),
    path('register/', views.Register, name='register'),

    path('editteam/', views.AddPlayertoTeam, name='editTeam'),
    path('player/<int:player_id>/', views.userPlayerStatistics, name='userPlayerStatistics'),

    path('leaderboard/', views.leaderBoard, name='leaderBoard'),
    path('budget/', views.userBudget, name='userBudget'),
]