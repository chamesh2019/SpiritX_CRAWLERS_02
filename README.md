# SpiritX CRAWLERS

## Overview

SpiritX CRAWLERS is a comprehensive Django-based web application designed to manage and display cricket player statistics, tournaments, and user interactions. The application includes an admin panel for managing players and a user interface for end-users to view and manage their teams. Additionally, it features real-time chat functionality and AI-based strategic suggestions.

## Features

### Admin Panel
- **Player Management**: Add, update, and delete player profiles.
- **Tournament Summary**: View total runs, total wickets, highest run scorer, and highest wicket-taker.

### User Interface
- **User Registration and Login**: Secure user authentication and registration.
- **Team Management**: Add and remove players from the user's team within budget constraints.
- **Player Statistics**: View detailed statistics of individual players.
- **Leaderboard**: Real-time leaderboard ranking users based on their team points.
- **Budget Overview**: Track user budget and total spent on players.

### Real-Time Chat
- **WebSocket Integration**: Real-time chat interface for user interactions.
- **AI-Based Suggestions**: AI assistant providing strategic team selection advice based on player statistics.

## Prerequisites

- Python 3.8+
- Django 5.1.7
- SQLite (default database)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/SpiritX_CRAWLERS.git
    cd SpiritX_CRAWLERS
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    Create a `.env` file in the root directory and add the following:
    ```
    SECRET_KEY='your-secret-key'
    DEBUG=True
    GEMINI_API_KEY='your-gemini-api-key'
    ```

5. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

6. Load sample data (optional):
    ```sh
    python import_data.py
    ```

7. Run the development server (uses daphne):
    ```sh
    daphne -p 8000 Spirit11.asgi:application
    ```

## Usage

### Admin Panel

- **Player Management**: Navigate to `/players/` to add, update, or delete players.
- **Tournament Summary**: View the tournament summary at `/players/tournamentSummery/`.

### User Interface

- **User Registration and Login**: Register at `/users/register/` and log in at `/users/login/`.
- **Team Management**: Manage your team at `/users/editteam/`.
- **Player Statistics**: View player statistics at `/users/player/<int:player_id>/`.
- **Leaderboard**: View the leaderboard at `/users/leaderboard/`.
- **Budget Overview**: View your budget overview at `/users/budget/`.

### Real-Time Chat

- **Chat Interface**: Access the chat interface at `/spiriter/` for real-time interactions and AI-based suggestions.

## API Endpoints

### Admin Panel

- `GET /players/`: View all players.
- `GET /players/<int:player_id>/`: View player statistics.
- `POST /players/addPlayer/`: Add a new player.
- `POST /players/<int:player_id>/update`: Update player information.
- `POST /players/deletePlayer/`: Delete a player.

### User Interface

- `GET /users/`: View user information and team.
- `POST /users/login/`: Log in a user.
- `POST /users/register/`: Register a new user.
- `POST /users/logout/`: Log out the user.
- `POST /users/editteam/`: Add or remove players from the user's team.
- `GET /users/leaderboard/`: View the leaderboard.
- `GET /users/budget/`: View the user's budget overview.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.