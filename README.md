# SpiritX CRAWLERS

## Overview

SpiritX CRAWLERS is a Django-based web application designed to manage and display cricket player statistics, tournaments, and user interactions. The application includes an admin panel for managing players and a user interface for end-users to view and manage their teams.

## Features

- Admin Panel for managing players
- User Interface for managing user teams
- Player statistics and tournament summaries
- User authentication and registration
- Leaderboard and budget overview for users

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
    ```

5. Apply the migrations:
    ```sh
    python [manage.py](http://_vscodecontentref_/0) migrate
    ```

6. Load sample data (optional):
    ```sh
    python [import_data.py](http://_vscodecontentref_/1)
    ```

7. Run the development server:
    ```sh
    python [manage.py](http://_vscodecontentref_/2) runserver
    ```

## Project Structure
SpiritX_CRAWLERS/
├── AdminPanel/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── playerView.html
│   │   ├── playerStatistics.html
│   │   ├── tournamentSummery.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── UserInterface/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── Login.html
│   │   ├── Register.html
│   │   ├── UserView.html
│   │   ├── budgetView.html
│   │   ├── leaderBoard.html
│   │   ├── userPlayerStatistics.html
│   │   ├── userPlayerView.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── Spirit11/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── .env
├── db.sqlite3
├── import_data.py
├── manage.py
├── requirements.txt
└── sample_data.csv

## Usage

### Admin Panel

- **Player Management**: Add, update, and delete players.
- **Tournament Summary**: View total runs, total wickets, highest run scorer, and highest wicket-taker.

### User Interface

- **User Registration and Login**: Register new users and log in existing users.
- **Team Management**: Add and remove players from the user's team.
- **Player Statistics**: View detailed statistics of individual players.
- **Leaderboard**: View the leaderboard of users based on their team points.
- **Budget Overview**: View the user's budget and total spent on players.

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

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.