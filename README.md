# **Tic Tac Toe**

This is a Python project that implements the classic Tic Tac Toe game in the terminal. The game offers two modes: **Play Alone** (against the computer with different difficulty levels) and **Play with a Friend** (multiplayer mode).

---

## **Features**

### **Game Modes**

1. **Play Alone:**

   * Face the computer with adjustable difficulties:

     * **Easy:** Basic moves.
     * **Medium:** Intermediate strategy.
     * **Hard:** Challenge your skills!
2. **Play with a Friend:**

   * Play a multiplayer match on the same computer.

### **Game Rules**

* The board consists of 9 positions numbered 1 to 9.
* Players alternate placing `X` and `O` marks.
* The winner is the one who aligns three of their marks horizontally, vertically, or diagonally.
* If all positions are filled without a winner, the game ends in a draw.

---

## **How to Play**

1. Run the program in the terminal.
2. Choose a mode from the main menu:

   * **1** to play against the computer.
   * **2** to play with a friend.
   * **3** to exit the game.
3. In **Play Alone** mode, select the difficulty level.
4. Enter the number corresponding to the desired position to make your move.
5. The scoreboard updates automatically after each round.

---

## **Board Layout Example**

Before each move, the board is displayed as follows:

```
 1  |  2  |  3  
----------------
 4  |  5  |  6  
----------------
 7  |  8  |  9  
```

After moves, the selected positions are replaced with `X` or `O`.

---

## **Dependencies**

* **Python 3.6+**
* `os` library (included in the standard Python distribution).

---

## **Notes**

1. The code is designed to run on Windows. The `cls` command used to clear the terminal screen is Windows-specific.
2. If you are using Linux or MacOS, replace the `cls` command with `clear` in the code to ensure the screen clears correctly:
   **1** Replace in the code:

   ```python
   os.system('cls')  # Windows
   ```

   **2** With:

   ```python
   os.system('clear')  # Linux/MacOS
   ```
3. This modification is necessary for the code to work properly on different operating systems.

---

## **How to Run**

1. Make sure Python 3 is installed on your system.
2. Download the source code and save it as `tic_tac_toe.py`.
3. Open the terminal and navigate to the directory where the file is saved.
4. Run the command:

   ```bash
   python tic_tac_toe.py
   ```

Have fun and enjoy the game! 😊
