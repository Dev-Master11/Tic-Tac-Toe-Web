**Tic-Tac-Toe Web App**

This is a simple Tic-Tac-Toe game built using Flask for the backend, with HTML, CSS, and JavaScript for the frontend. The game lets a player compete against a computer opponent.

### Features:
- Single-player mode (play against the computer).
- Dynamic game board with JavaScript for real-time updates.
- Flask backend to handle the game logic.
- AJAX requests for smooth, responsive gameplay.
- Responsive UI with CSS styling for better user experience.
- Restart functionality to play again.

### Tech Stack:
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)

### Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/Dev-Master11/Tic-Tac-Toe-Web.git
   cd Tic-Tac-Toe-Web
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask
   ```

### Running the Game:
1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

### How to Play:
- The game starts with Player X (you) against the Computer (O).
- Click on any available cell to make your move.
- The computer will automatically make its move.
- The game ends when a player wins or if it’s a draw.
- To restart the game, click the "Restart Game" button.

### Project Structure:
```
/tic_tac_toe
│-- /static
│   │-- style.css       # Styles for the game board
│   │-- script.js       # JavaScript for game logic
│-- /templates
│   │-- index.html      # Frontend UI
│-- app.py              # Flask backend
│-- README.md           # Project documentation
```
