from django.urls import path

from . import views

urlpatterns = [
    path('', views.playerView, name='playerView'),
    path('<int:player_id>/', views.playerStatistics, name='playerStatistics'),
    path('tournamentSummery/', views.tournamentSummery, name='tournamentSummery'),

    path('addPlayer/', views.addPlayer, name='addPlayer'),
    path('<int:player_id>/update', views.updatePlayer, name='updatePlayer'),
    path('deletePlayer/', views.deletePlayer, name='deletePlayer'),

]
