from django.db import models


class Team(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, null=False)
    league = models.ForeignKey('League', on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)

    def __str__(self):
        return ", ".join([
            self.timestamp.strftime("%Y-%m-%d"),
            self.name, self.league.title, 'Wins: ' + str(self.wins), 'Goals: ' + str(self.goals)
                          ])


class Match(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    opponent_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='opponent_team')

    def __str__(self):
        return ", ".join([self.timestamp.strftime("%Y-%m-%d"), 'Match info: \n',
                          'Home team: ' + self.home_team.name,
                          'Opponent team: ' + self.opponent_team.name
                          ])


class Result(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    score_home_team = models.IntegerField(default=0)
    score_opponents_team = models.IntegerField(default=0)

    def __str__(self):
        return ", ".join([self.match.timestamp.strftime("%Y-%m-%d"), 'Match result details: \n',
                          self.match.home_team.name + ': ' + str(self.score_home_team),
                          self.match.opponent_team.name + ': ' + str(self.score_opponents_team),
                          ])


class League(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return ", ".join([self.timestamp.strftime("%Y-%m-%d"), 'League name: ' + self.title])
