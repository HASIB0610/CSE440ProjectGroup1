# Tic-Tac-Toe AI – Minimax with Alpha-Beta Pruning

This is a simple **Tic-Tac-Toe game with an AI opponent** that uses the  
**Minimax algorithm** and **Alpha-Beta pruning** to make decisions.

The project was built as part of our **Artificial Intelligence** course.  
The focus is on **game tree search**, **decision making**, and **difficulty control** using search depth and heuristic evaluation.

---

## Features

- Human vs AI Tic-Tac-Toe (3×3 board)
- AI uses:
  - **Minimax algorithm**
  - **Alpha-Beta pruning** for efficiency
  - **Heuristic evaluation** at limited depth
- **Three difficulty levels**:
  - Easy – shallow search (makes mistakes)
  - Medium – deeper search with better play
  - Hard – deep search, close to optimal play
- Command-line interface (no external libraries required)

---

## How the AI Works (Short Explanation)

1. The board is represented as a list of 9 cells:  
   `[" ", " ", " ", " ", " ", " ", " ", " ", " "]`

2. The AI simulates all possible future moves using **Minimax**:
   - When it’s AI’s turn → it tries to **maximize** the score.
   - When it’s the opponent’s turn → it tries to **minimize** the score.

3. Game outcomes are scored as:
   - AI win → positive score (e.g., `10 - depth`)
   - Draw → `0`
   - AI loss → negative score (e.g., `depth - 10`)

4. **Alpha-Beta pruning** skips branches that cannot affect the final decision,  
   which makes the search faster.

5. For **Easy/Medium** difficulty, a **depth cutoff** is used:
   - When the search reaches the cutoff depth, the AI stops looking deeper
   - It then uses a **heuristic function** to estimate how good the board is

---

## Difficulty Levels

When the game starts, the player selects one difficulty:

- **Easy (cutoff = 2)**  
  AI looks only a few moves ahead → can miss winning or blocking moves.

- **Medium (cutoff = 4)**  
  AI looks deeper → plays better and makes fewer mistakes.

- **Hard (higher or no cutoff)**  
  AI searches much deeper and plays close to perfectly.

Internally, difficulty is controlled by changing the **max search depth (cutoff)** passed into the `minimax()` function.

---

## 📁 Project Structure

### **main.py**
- Asks the user to choose X/O  
- Shows board positions (1–9)  
- Asks for difficulty level (Easy / Medium / Hard)  
- Starts and repeats the game loop  

### **tictactoe_game.py**
- `print_board(board)` – prints the 3×3 Tic-Tac-Toe board  
- `player_move(board, human_player)` – handles the human player's input  
- `ai_move(board, ai_player, use_heuristic, cutoff)` – calls the Minimax function and updates the board  

### **tictactoe_ai.py**
- `check_winner(board)` – checks for win/draw/ongoing game  
- `heuristic(board, player)` – assigns scores to board states for non-terminal evaluation  
- `legal_moves(board)` / `ordered_moves(board)` – generates valid moves, prioritizing strong positions  
- `minimax(...)` – core AI algorithm with alpha-beta pruning and optional depth cutoff for difficulty  

---

## How to Run

### **1. Requirements**
- Python **3.x**
- No external libraries required

### **2. Steps**

```bash
# Clone this repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Run the game
python main.py
