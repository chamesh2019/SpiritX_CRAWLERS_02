import django
django.setup()

import pandas as pd
from AdminPanel.models import Player

csv_file_path = 'sample_data.csv'
df = pd.read_csv(csv_file_path)


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