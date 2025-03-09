import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Spirit11.settings')
django.setup()

import pandas as pd
from AdminPanel.models import Player
from UserInterface.models import EndUser, Token

if input("This will delete all the data in the database and revert it to default. Are you sure you want to continue? (yes/no): ") != 'yes':
    exit()

csv_file_path = 'sample_data.csv'
df = pd.read_csv(csv_file_path)

Player.objects.all().delete()

for index, row in df.iterrows():
    player = Player(
        name = row['Name'],
        university = row['University'],
        category = row['Category'],
        total_runs = row['Total Runs'],
        balls_faced = row['Balls Faced'],
        innings_played = row['Innings Played'],
        wickets = row['Wickets'],
        overs_bowled = row['Overs Bowled'],
        runs_given = row['Runs Conceded']
    )
    player.save()

print("CSV data has been loaded into the Django database.")

EndUser.objects.all().delete()

user = EndUser.objects.create(name='spiritx_2025', type='user', password='SpiritX@2025')
user.save()

sample_player_names = [
    'Danushka Kumara',
    'Jeewan Thirimanne',
    'Charith Shanaka',
    'Pathum Dhananjaya',
    'Suranga Bandara',
    'Sammu Sandakan', 
    'Minod Rathnayake',
    'Lakshan Gunathilaka',
    'Sadeera Rajapaksa', 
    'Danushka Jayawickrama', 
    'Lakshan Vandersay'
]

player_set = Player.objects.filter(name__in=sample_player_names)
user.players.set(player_set)
user.budget = user.budget - sum([player.get_value() for player in player_set])
user.save()

user = EndUser.objects.create(name='admin', type='admin', password='admin')
user.save()

default_message = """
Successfully loaded the default data into the database.
The default data includes:
- players with their statistics
- an end user with a team of 11 players - spiritx_2025:SpiritX@2025
- an admin user - admin:admin
"""

print(default_message)