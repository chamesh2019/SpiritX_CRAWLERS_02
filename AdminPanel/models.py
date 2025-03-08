from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    total_runs = models.IntegerField()
    balls_faced = models.IntegerField()
    innings_played = models.IntegerField()
    wickets = models.IntegerField()
    overs_bowled = models.IntegerField()
    runs_given = models.IntegerField()

    def get_points(self):
        batting_strike_rate = (self.total_runs / self.balls_faced) * 100 if self.balls_faced != 0 else 0
        bowling_strike_rate = (self.overs_bowled * 6) / self.wickets if self.wickets != 0 else 0
        economy_rate = self.runs_given / self.overs_bowled if self.overs_bowled != 0 else 0
        batting_average = self.total_runs / self.innings_played if self.innings_played != 0 else 0

        self_points = (batting_strike_rate / 5)
        self_points += (batting_average * 0.8)
        self_points += (500 / bowling_strike_rate) if bowling_strike_rate != 0 else 0
        self_points += (140 / economy_rate) if economy_rate != 0 else 0

        return self_points
    
    def get_value(self):
        self_points = self.get_points()
        self_value = (self_points * 9 + 100) * 1000 
        self_value = round(self_value / 50000) * 50000

        return self_value