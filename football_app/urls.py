"""football_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from football_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('maxWins/<str:league_name>/', views.max_wins, name='max_wins'),
    path('minWins/<str:league_name>/', views.min_wins, name='min_wins'),
    path('maxGoals/<str:league_name>/', views.max_goals, name='max_goals'),
    path('minGoals/<str:league_name>/', views.min_goals, name='min_goals'),
    path('league/<str:league_name>/', views.create_league, name='create_league'),
    path('team/<str:league_name>/<str:name>/', views.create_team, name='create_team'),
    path('match/<str:home_team_name>/<str:opp_team_name>/<int:home_team_score>/<int:opp_team_score>/'
         , views.create_match, name='create_match'),

]


