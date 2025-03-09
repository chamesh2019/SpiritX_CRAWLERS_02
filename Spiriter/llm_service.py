import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

def generate_dataset(players, user):
    
    dataset = ""
    for player in players:
        dataset += f"Player: {player.name}\n"
        dataset += f"University: {player.university}\n"
        dataset += f"Category: {player.category}\n"
        dataset += f"Total Runs: {player.total_runs}\n"
        dataset += f"Balls Faced: {player.balls_faced}\n"
        dataset += f"Innings Played: {player.innings_played}\n"
        dataset += f"Wickets: {player.wickets}\n"
        dataset += f"Overs Bowled: {player.overs_bowled}\n"
        dataset += f"Runs Given: {player.runs_given}\n"
        dataset += f"Player Price: {player.get_value()}\n\n"

    userdata = ""
    userdata += f"User Name: {user.name}\n"
    userdata += f"User Budget: {user.budget}\n"
    userdata += f"Current Team: {', '.join([player.name for player in user.players.all()])}\n"
    userdata += f"Team Size: {user.players.count()}\n"

    
    sys_instructions = f'''
    "You are Spiriter, an AI assistant for a fantasy cricket league. Your role is to help users make strategic team selections based on player statistics. Use the given dataset to provide accurate information about players. Follow these rules strictly:

    1️⃣ Player Queries: If a user asks about a player's details, respond with only the available dataset information (e.g., runs, wickets, team). Do not generate or assume stats.
    2️⃣ Team Suggestions: When asked to suggest a team, select the best possible team of 11 players with the highest points, ensuring budget constraints are met.
    3️⃣ Restricted Information: Never reveal player points directly. Use points only internally for calculations.
    4️⃣ Unknown Data: If a user asks for unavailable details, respond with: ‘I don’t have enough knowledge to answer that question.’
    5️⃣ General Queries: If asked about cricket rules or strategies, provide generic insights, but never make assumptions about real-world ongoing matches.
    6️⃣ Engagement: Keep responses concise and friendly, guiding users efficiently.

    Here is the User's information:

    {userdata}
    
    Now, proceed with answering the user's query based on the dataset."**

    {dataset}

    '''
    return sys_instructions


def generate_content(contents, players, user):
    load_dotenv()
    client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=contents,
        config=types.GenerateContentConfig(
        system_instruction=generate_dataset(players, user)),
    )
    return response.text