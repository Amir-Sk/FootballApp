from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from football_app.models import Team, League, Match, Result


def index(request, template='index.html'):
    return render(request, template,)


def max_goals(request, league_name):
    try:
        team = Team.objects.filter(league=get_league(league_name)).order_by('goals').last()
        return HttpResponse(content=team)
    except ObjectDoesNotExist as err:
        return print_error_and_respond(err, 404)


def min_goals(request, league_name):
    try:
        team = Team.objects.filter(league=get_league(league_name)).order_by('goals').first()
        return HttpResponse(content=team)
    except ObjectDoesNotExist as err:
        return print_error_and_respond(err, 404)


def max_wins(request, league_name):
    try:
        team = Team.objects.filter(league=get_league(league_name)).order_by('wins').last()
        return HttpResponse(team)
    except ObjectDoesNotExist as err:
        return print_error_and_respond(err, 404)


def min_wins(request, league_name):
    try:
        league = get_league(league_name)
        if league is None:
            result = "No league found using: {}".format(league_name)
        else:
            result = team = Team.objects.filter(league=get_league(league_name)).order_by('wins').first()
        return HttpResponse(result)
    except Exception as err:
        print("Exception encountered:".format(err))
        return HttpResponse(status=500)


def create_match(request, home_team_name, opp_team_name, home_team_score, opp_team_score):
    try:
        home_team = Team.objects.get(name=home_team_name)
        opp_team = Team.objects.get(name=opp_team_name)
        match = Match(timestamp=timezone.now(), home_team=home_team, opponent_team=opp_team)
        match.save()
        print("Created match: \n {}".format(match))
        game_result = Result(match=match, score_home_team=home_team_score, score_opponents_team=opp_team_score)
        game_result.save()
        print("Created game result: \n {}".format(game_result))
        update_stats(home_team, opp_team, home_team_score, opp_team_score)
        return HttpResponse(match)
    except ObjectDoesNotExist as err:
        return print_error_and_respond(err, 404)


def create_team(request, league_name, name):
    try:
        league = get_league(league_name)
        team = Team.objects.get_or_create(league=league, name=name)
        print("Created team: \n {}".format(team))
        return HttpResponse(team)
    except ObjectDoesNotExist as err:
        return print_error_and_respond(err, 404)
    except Exception as err:
        print_error_and_respond(err, 500)


def create_league(request, league_name):
    try:
        league = League.objects.get_or_create(title=league_name)
        print("Created League: ", league)
        return HttpResponse(league)
    except Exception as err:
        print_error_and_respond(err, 500)


def get_league(league_name):
    try:
        return League.objects.get(title=league_name)
    except ObjectDoesNotExist as err:
        return print_error_and_respond(err, 404)
    except Exception as err:
        print_error_and_respond(err, 500)


def print_error_and_respond(err, status):
    print("Exception encountered:".format(err))
    return HttpResponse(err, status=status)


def update_stats(home_team, opp_team, home_team_score, opp_team_score):
    if home_team_score > opp_team_score:
        update_win(home_team)
    elif home_team_score < opp_team_score:
        update_win(opp_team)
    update_goals(home_team, home_team_score, opp_team, opp_team_score)


def update_goals(home_team, home_team_score, opp_team, opp_team_score):
    home_team.goals = home_team.goals + home_team_score
    opp_team.goals = opp_team.goals + opp_team_score
    opp_team.save()
    home_team.save()


def update_win(team):
    team.wins = team.wins + 1
    team.save()