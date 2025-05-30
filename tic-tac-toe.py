import os
import random
import time

def Play_Alone(difficulty):
    """
    Plays a game of Tic-Tac-Toe against a computer opponent.

    Args:
        difficulty (int): The difficulty level of the AI (1: Easy, 2: Medium, 3: Hard).
    """

    if difficulty == 1:  # Easy difficulty
        player_score = 0
        robot_score = 0

        while True:
            os.system('cls')  # Clear the console
            # Initialize board numbers
            N1, N2, N3 = 1, 2, 3
            N4, N5, N6 = 4, 5, 6
            N7, N8, N9 = 7, 8, 9

            # Display scores
            score_display = f'* Score *\nYou: {player_score}\nRobot: {robot_score}\n\n' [cite: 2]
            # Display Tic-Tac-Toe board
            board_layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n' [cite: 3, 4, 5]

            print(score_display) [cite: 2]
            print(board_layout) [cite: 3, 4, 5]

            continue_game = int(input('\nStart game:\n1- Yes\n2- No\nR: ')) [cite: 5]
            while continue_game != 1 and continue_game != 2: [cite: 5]
                continue_game = int(input('\nInvalid option!\nStart game:\n1- Yes\n2- No\nR: ')) [cite: 5]

            if continue_game == 2: [cite: 6]
                break

            while True:
                while True:
                    os.system('cls') # Clear the console

                    score_display = f'* Score *\nYou: {player_score}\nRobot: {robot_score}\n\n' [cite: 7]
                    board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 8, 9]

                    print(score_display) [cite: 7]
                    print(board_layout) [cite: 8, 9]

                    player1_move = int(input('\nPlayer ONE turn\nR: ')) [cite: 9]
                    while player1_move > 9 or player1_move < 1: [cite: 9]
                        player1_move = int(input('\nInvalid option! Enter a number from 1 to 9\nPlayer ONE turn\nR: ')) [cite: 10]

                    # Update board with player's move ('X')
                    if player1_move == N1 and N1 == 1: [cite: 10]
                        N1 = 'X' [cite: 10]
                        break [cite: 11]
                    elif player1_move == N2 and N2 == 2: [cite: 11]
                        N2 = 'X' [cite: 11]
                        break [cite: 11]
                    elif player1_move == N3 and N3 == 3: [cite: 12]
                        N3 = 'X' [cite: 12]
                        break [cite: 12]
                    elif player1_move == N4 and N4 == 4: [cite: 12]
                        N4 = 'X' [cite: 13]
                        break [cite: 13]
                    elif player1_move == N5 and N5 == 5: [cite: 13]
                        N5 = 'X' [cite: 13]
                        break [cite: 14]
                    elif player1_move == N6 and N6 == 6: [cite: 14]
                        N6 = 'X' [cite: 14]
                        break [cite: 14]
                    elif player1_move == N7 and N7 == 7: [cite: 15]
                        N7 = 'X' [cite: 15]
                        break [cite: 15]
                    elif player1_move == N8 and N8 == 8: [cite: 15, 16]
                        N8 = 'X' [cite: 16]
                        break [cite: 16]
                    elif player1_move == N9 and N9 == 9: [cite: 16]
                        N9 = 'X' [cite: 17]
                        break [cite: 17]
                    else: # Invalid move (position already taken)
                        go_back = int(input('\nCannot select an already used position!\nEnter "1" to go back\nR: ')) [cite: 17]
                        while go_back != 1: [cite: 18]
                            go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 18]

                os.system('cls') # Clear the console

                score_display = f'* Score *\nYou: {player_score}\nRobot: {robot_score}\n\n' [cite: 18]
                board_layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  | {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n' [cite: 19, 20]

                print(score_display) [cite: 18]
                print(board_layout) [cite: 19, 20]

                # Check for player win
                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or \
                   (N4 == 'X' and N5 == 'X' and N6 == 'X') or \
                   (N7 == 'X' and N8 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N4 == 'X' and N7 == 'X') or \
                   (N2 == 'X' and N5 == 'X' and N8 == 'X') or \
                   (N3 == 'X' and N6 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N5 == 'X' and N9 == 'X') or \
                   (N3 == 'X' and N5 == 'X' and N7 == 'X'): [cite: 20, 21]
                    print('\n\n* Congratulations *\nYou won!') [cite: 21]
                    player_score += 1 [cite: 21]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 22]
                    while go_back != 1: [cite: 22]
                        go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 22]

                    break [cite: 23]

                # Check for robot win
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or \
                   (N4 == 'O' and N5 == 'O' and N6 == 'O') or \
                   (N7 == 'O' and N8 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N4 == 'O' and N7 == 'O') or \
                   (N2 == 'O' and N5 == 'O' and N8 == 'O') or \
                   (N3 == 'O' and N6 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N5 == 'O' and N9 == 'O') or \
                   (N3 == 'O' and N5 == 'O' and N7 == 'O'): [cite: 23, 24]
                    print('\n\n* Too bad! *\nRobot won!') [cite: 24, 25]
                    robot_score += 1 [cite: 25]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 25]
                    while go_back != 1: [cite: 25, 26]
                        go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 26]

                    break [cite: 26]

                # Check for a tie
                if N1 != 1 and N2 != 2 and N3 != 3 and \
                   N4 != 4 and N5 != 5 and N6 != 6 and \
                   N7 != 7 and N8 != 8 and N9 != 9: [cite: 26]
                    print('\nGame tied!') [cite: 27]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 27]
                    while go_back != 1: [cite: 27]
                        go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 27]

                    break [cite: 28]

                # Robot's turn (Easy difficulty - random moves)
                while True:
                    # The original code's AI logic for difficulty 1 seems to be mostly random,
                    # with some attempts to prioritize rows/columns/diagonals where the player has a mark.
                    # This behavior is less strategic and more akin to random play.
                    if (N1 == 'X' or N2 == 'X' or N3 == 'X') and (N1 != 'X' or N2 != 'X' or N3 != 'X'): [cite: 28]
                        robot_move = random.randint(1, 3) [cite: 29]
                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'): [cite: 29]
                        robot_move = random.randint(4, 6) [cite: 29]
                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'): # Duplicate condition [cite: 30]
                        robot_move = random.randint(7, 9) [cite: 30]
                    elif (N1 == 'X' or N5 == 'X' or N9 == 'X') and (N1 != 'X' or N5 != 'X' or N9 != 'X'): [cite: 30]
                        num = random.randint(1, 3) [cite: 31]
                        if num == 1: [cite: 31]
                            robot_move = 1 [cite: 31]
                        elif num == 2: [cite: 31, 32]
                            robot_move = 5 [cite: 32]
                        else: [cite: 32]
                            robot_move = 9 [cite: 32]
                    elif (N3 == 'X' or N5 == 'X' or N7 == 'X') and (N3 != 'X' or N5 != 'X' or N7 != 'X'): [cite: 33]
                        num = random.randint(1, 3) [cite: 33]
                        if num == 1: [cite: 33]
                            robot_move = 3 [cite: 34]
                        elif num == 2: [cite: 34]
                            robot_move = 5 [cite: 34]
                        else: [cite: 34, 35]
                            robot_move = 7 [cite: 35]
                    elif (N1 == 'X' or N4 == 'X' or N7 == 'X') and (N1 != 'X' or N4 != 'X' or N7 != 'X'): [cite: 35]
                        num = random.randint(1, 3) [cite: 35]
                        if num == 1: [cite: 36]
                            robot_move = 1 [cite: 36]
                        elif num == 2: [cite: 36, 37]
                            robot_move = 4 [cite: 37]
                        else: [cite: 37]
                            robot_move = 7 [cite: 37]
                    elif (N2 == 'X' or N5 == 'X' or N8 == 'X') and (N2 != 'X' or N5 != 'X' or N8 != 'X'): [cite: 37, 38]
                        num = random.randint(1, 3) [cite: 38]
                        if num == 1: [cite: 38]
                            robot_move = 2 [cite: 38]
                        elif num == 2: [cite: 39]
                            robot_move = 5 [cite: 39]
                        else: [cite: 39]
                            robot_move = 8 [cite: 39]
                    elif (N3 == 'X' or N6 == 'X' or N9 == 'X') and (N3 != 'X' or N6 != 'X' or N9 != 'X'): [cite: 40]
                        num = random.randint(1, 3) [cite: 40]
                        if num == 1: [cite: 41]
                            robot_move = 3 [cite: 41]
                        elif num == 2: [cite: 41]
                            robot_move = 6 [cite: 41]
                        else: [cite: 42]
                            robot_move = 9 [cite: 42]
                    else: # If no specific condition met, choose a random empty spot
                        robot_move = random.randint(1, 9) [cite: 42]

                    # Update board with robot's move ('O')
                    if robot_move == N1 and N1 == 1: [cite: 43]
                        N1 = 'O' [cite: 43]
                        break [cite: 43]
                    elif robot_move == N2 and N2 == 2: [cite: 43]
                        N2 = 'O' [cite: 44]
                        break [cite: 44]
                    elif robot_move == N3 and N3 == 3: [cite: 44]
                        N3 = 'O' [cite: 45]
                        break [cite: 45]
                    elif robot_move == N4 and N4 == 4: [cite: 45]
                        N4 = 'O' [cite: 45]
                        break [cite: 45]
                    elif robot_move == N5 and N5 == 5: [cite: 46]
                        N5 = 'O' [cite: 46]
                        break [cite: 46]
                    elif robot_move == N6 and N6 == 6: [cite: 46]
                        N6 = 'O' [cite: 47]
                        break [cite: 47]
                    elif robot_move == N7 and N7 == 7: [cite: 47]
                        N7 = 'O' [cite: 48]
                        break [cite: 48]
                    elif robot_move == N8 and N8 == 8: [cite: 48]
                        N8 = 'O' [cite: 48]
                        break [cite: 49]
                    elif robot_move == N9 and N9 == 9: [cite: 49]
                        N9 = 'O' [cite: 49]
                        break [cite: 49]

                print(f'\nRobot chose position {robot_move}') [cite: 49]
                time.sleep(3) # Pause for 3 seconds [cite: 50]

                os.system('cls') # Clear the console

                score_display = f'* Score *\nYou: {player_score}\nRobot: {robot_score}\n\n' [cite: 50]
                board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 51, 52]

                print(score_display) [cite: 50]
                print(board_layout) [cite: 51, 52]

                # Check for player win after robot's move
                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or \
                   (N4 == 'X' and N5 == 'X' and N6 == 'X') or \
                   (N7 == 'X' and N8 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N4 == 'X' and N7 == 'X') or \
                   (N2 == 'X' and N5 == 'X' and N8 == 'X') or \
                   (N3 == 'X' and N6 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N5 == 'X' and N9 == 'X') or \
                   (N3 == 'X' and N5 == 'X' and N7 == 'X'): [cite: 52, 53]
                    print('\n\n* Congratulations *\nYou won!') [cite: 53]
                    player_score += 1 [cite: 53]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 54]
                    while go_back != 1: [cite: 54]
                        go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 54]

                    break [cite: 55]

                # Check for robot win after robot's move
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or \
                   (N4 == 'O' and N5 == 'O' and N6 == 'O') or \
                   (N7 == 'O' and N8 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N4 == 'O' and N7 == 'O') or \
                   (N2 == 'O' and N5 == 'O' and N8 == 'O') or \
                   (N3 == 'O' and N6 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N5 == 'O' and N9 == 'O') or \
                   (N3 == 'O' and N5 == 'O' and N7 == 'O'): [cite: 55, 56]
                    print('\n\n* Too bad! *\nRobot won!') [cite: 56, 57]
                    robot_score += 1 [cite: 57]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 57]
                    while go_back != 1: [cite: 57, 58]
                        go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 58]

                    break [cite: 58]

                # Check for a tie after robot's move
                if N1 != 1 and N2 != 2 and N3 != 3 and \
                   N4 != 4 and N5 != 5 and N6 != 6 and \
                   N7 != 7 and N8 != 8 and N9 != 9: [cite: 58]
                    print('\nGame tied!') [cite: 59]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 59]
                    while go_back != 1: [cite: 59]
                        go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 59]

                    break [cite: 60]

    elif difficulty == 2:  # Medium difficulty
        player_score = 0
        robot_score = 0

        while True:
            os.system('cls')
            # Initialize board numbers
            N1, N2, N3 = 1, 2, 3
            N4, N5, N6 = 4, 5, 6
            N7, N8, N9 = 7, 8, 9 [cite: 60, 61, 62]

            score_display = f'* Score *\nYou: {player_score}\nRobot: {robot_score}\n\n' [cite: 62]
            board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 62, 63, 64]

            print(score_display) [cite: 62]
            print(board_layout) [cite: 62, 63, 64]

            continue_game = int(input('\nStart game:\n1- Yes\n2- No\nR: ')) [cite: 64]
            while continue_game != 1 and continue_game != 2: [cite: 64]
                continue_game = int(input('\nInvalid option!\nStart game:\n1- Yes\n2- No\nR: ')) [cite: 64]

            if continue_game == 2: [cite: 65]
                break

            while True:
                while True:
                    os.system('cls')

                    score_display = f'* Score *\nYou: {player_score}\nBot: {robot_score}\n\n' [cite: 66]
                    board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 67, 68]

                    print(score_display) [cite: 66]
                    print(board_layout) [cite: 67, 68]

                    player1_move = int(input('\nYour turn\nR: ')) [cite: 68]
                    while player1_move > 9 or player1_move < 1: [cite: 68]
                        player1_move = int(input('\nInvalid option! Enter a number from 1 to 9\nYour turn\nR: ')) [cite: 69]

                    # Update board with player's move ('X')
                    if player1_move == N1 and N1 == 1: [cite: 69]
                        N1 = 'X' [cite: 69]
                        break [cite: 70]
                    elif player1_move == N2 and N2 == 2: [cite: 70]
                        N2 = 'X' [cite: 70]
                        break [cite: 70]
                    elif player1_move == N3 and N3 == 3: [cite: 71]
                        N3 = 'X' [cite: 71]
                        break [cite: 71]
                    elif player1_move == N4 and N4 == 4: [cite: 71]
                        N4 = 'X' [cite: 72]
                        break [cite: 72]
                    elif player1_move == N5 and N5 == 5: [cite: 72]
                        N5 = 'X' [cite: 72]
                        break [cite: 73]
                    elif player1_move == N6 and N6 == 6: [cite: 73]
                        N6 = 'X' [cite: 73]
                        break [cite: 73]
                    elif player1_move == N7 and N7 == 7: [cite: 74]
                        N7 = 'X' [cite: 74]
                        break [cite: 74]
                    elif player1_move == N8 and N8 == 8: [cite: 74, 75]
                        N8 = 'X' [cite: 75]
                        break [cite: 75]
                    elif player1_move == N9 and N9 == 9: [cite: 75]
                        N9 = 'X' [cite: 76]
                        break [cite: 76]
                    else:
                        go_back = int(input('\nCannot select an already used position!\nEnter "1" to go back\nR: ')) [cite: 76]
                        while go_back != 1: [cite: 77]
                            go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 77]

                os.system('cls')

                score_display = f'* Score *\nYou: {player_score}\nRobot: {robot_score}\n\n' [cite: 77]
                board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 78, 79]

                print(score_display) [cite: 77]
                print(board_layout) [cite: 78, 79]

                # Check for player win
                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or \
                   (N4 == 'X' and N5 == 'X' and N6 == 'X') or \
                   (N7 == 'X' and N8 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N4 == 'X' and N7 == 'X') or \
                   (N2 == 'X' and N5 == 'X' and N8 == 'X') or \
                   (N3 == 'X' and N6 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N5 == 'X' and N9 == 'X') or \
                   (N3 == 'X' and N5 == 'X' and N7 == 'X'): [cite: 79, 80]
                    print('\n\n* Congratulations *\nYou won!') [cite: 80]
                    player_score += 1 [cite: 80]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 81]
                    while go_back != 1: [cite: 81]
                        go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 81]

                    break [cite: 82]

                # Check for robot win
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or \
                   (N4 == 'O' and N5 == 'O' and N6 == 'O') or \
                   (N7 == 'O' and N8 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N4 == 'O' and N7 == 'O') or \
                   (N2 == 'O' and N5 == 'O' and N8 == 'O') or \
                   (N3 == 'O' and N6 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N5 == 'O' and N9 == 'O') or \
                   (N3 == 'O' and N5 == 'O' and N7 == 'O'): [cite: 82, 83]
                    print('\n\n* Too bad! *\nRobot won!') [cite: 83, 84]
                    robot_score += 1 [cite: 84]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 84]
                    while go_back != 1: [cite: 84, 85]
                        go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 85]

                    break [cite: 85]

                # Check for a tie
                if N1 != 1 and N2 != 2 and N3 != 3 and \
                   N4 != 4 and N5 != 5 and N6 != 6 and \
                   N7 != 7 and N8 != 8 and N9 != 9: [cite: 85]
                    print('\nGame tied!') [cite: 86]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 86]
                    while go_back != 1: [cite: 86]
                        go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 86]

                    break [cite: 87]

                # Robot's turn (Medium difficulty - attempts to block player's winning moves)
                while True:
                    # Check if player is about to win and block
                    if ((N1 == 'X' and N2 == 'X' and N3 != 'O') or \
                        (N1 == 'X' and N3 == 'X' and N2 != 'O') or \
                        (N2 == 'X' and N3 == 'X' and N1 != 'O')) and \
                       (N1 != 'X' or N2 != 'X' or N3 != 'X'): [cite: 87, 88]
                        robot_move = random.randint(1, 3) [cite: 88] # Randomly chooses a spot in that row

                    elif ((N4 == 'X' and N5 == 'X' and N6 != 'O') or \
                          (N4 == 'X' and N6 == 'X' and N6 != 'O') or \
                          (N5 == 'X' and N6 == 'X' and N4 != 'O')) and \
                         (N4 != 'X' or N5 != 'X' or N6 != 'X'): [cite: 88, 89]
                        robot_move = random.randint(4, 6) [cite: 89]

                    elif ((N7 == 'X' and N8 == 'X' and N9 != 'O') or \
                          (N7 == 'X' and N9 == 'X' and N8 != 'O') or \
                          (N8 == 'X' and N9 == 'X' and N7 != 'O')) and \
                         (N7 != 'X' or N8 != 'X' or N9 != 'X'): [cite: 89, 90]
                        robot_move = random.randint(7, 9) [cite: 90]

                    elif ((N1 == 'X' and N4 == 'X' and N7 != 'O') or \
                          (N1 == 'X' and N7 == 'X' and N4 != 'O') or \
                          (N4 == 'X' and N7 == 'X' and N1 != 'O')) and \
                         (N1 != 'X' or N4 != 'X' or N7 != 'X'): [cite: 90]
                        while True:
                            num = random.randint(1, 3) [cite: 91]
                            if num == 1 and N1 != 'X': [cite: 91]
                                robot_move = 1 [cite: 92]
                                break
                            elif num == 2 and N4 != 'X': [cite: 92, 93]
                                robot_move = 4 [cite: 93]
                                break
                            elif num == 3 and N7 != 'X': [cite: 93, 94]
                                robot_move = 7 [cite: 94]
                                break
                            else: [cite: 94]
                                break [cite: 95]

                    elif ((N2 == 'X' and N5 == 'X' and N8 != 'O') or \
                          (N2 == 'X' and N8 == 'X' and N5 != 'O') or \
                          (N5 == 'X' and N8 == 'X' and N2 != 'O')) and \
                         (N2 != 'X' or N5 != 'X' or N8 != 'X'): [cite: 95, 96]
                        while True:
                            num = random.randint(1, 3) [cite: 96]
                            if num == 1 and N2 != 'X': [cite: 96, 97]
                                robot_move = 2 [cite: 97]
                                break
                            elif num == 2 and N5 != 'X': [cite: 97, 98]
                                robot_move = 5 [cite: 98]
                                break
                            elif num == 3 and N8 != 'X': [cite: 98, 99]
                                robot_move = 8 [cite: 99]
                                break
                            else: [cite: 99]
                                break [cite: 99]

                    elif ((N3 == 'X' and N6 == 'X' and N9 != 'O') or \
                          (N3 == 'X' and N9 == 'X' and N6 != 'O') or \
                          (N6 == 'X' and N9 == 'X' and N3 != 'O')) and \
                         (N3 != 'X' or N6 != 'X' or N9 != 'X'): [cite: 100]
                        while True:
                            num = random.randint(1, 3) [cite: 101]
                            if num == 1 and N3 != 'X': [cite: 101]
                                robot_move = 3 [cite: 101]
                                break [cite: 102]
                            elif num == 2 and N6 != 'X': [cite: 102]
                                robot_move = 6 [cite: 102]
                                break [cite: 103]
                            elif num == 3 and N9 != 'X': [cite: 103]
                                robot_move = 9 [cite: 103]
                                break [cite: 104]
                            else: [cite: 104]
                                break [cite: 104]

                    elif ((N1 == 'X' and N5 == 'X' and N9 != 'O') or \
                          (N1 == 'X' and N9 == 'X' and N5 != 'O') or \
                          (N5 == 'X' and N9 == 'X' and N1 != 'O')) and \
                         (N1 != 'X' or N5 != 'X' or N9 != 'X'): [cite: 105]
                        while True:
                            num = random.randint(1, 3) [cite: 106]
                            if num == 1 and N1 != 'X': [cite: 106]
                                robot_move = 1 [cite: 106]
                                break [cite: 107]
                            elif num == 2 and N5 != 'X': [cite: 107]
                                robot_move = 5 [cite: 107]
                                break [cite: 108]
                            elif num == 3 and N9 != 'X': [cite: 108]
                                robot_move = 9 [cite: 108]
                                break [cite: 109]
                            else: [cite: 109]
                                break [cite: 109]

                    elif ((N3 == 'X' and N5 == 'X' and N7 != 'O') or \
                          (N3 == 'X' and N7 == 'X' and N5 != 'O') or \
                          (N7 == 'X' and N5 == 'X' and N3 != 'O')) and \
                         (N3 != 'X' or N5 != 'X' or N7 != 'X'): [cite: 109, 110]
                        while True:
                            num = random.randint(1, 3) [cite: 110, 111]
                            if num == 1 and N3 != 'X': [cite: 111]
                                robot_move = 3 [cite: 111]
                                break
                            elif num == 2 and N5 != 'X': [cite: 112]
                                robot_move = 5 [cite: 112]
                                break
                            elif num == 3 and N7 != 'X': [cite: 113]
                                robot_move = 7 [cite: 113]
                                break
                            else: [cite: 114]
                                break [cite: 114]

                    # These conditions seem to represent "if player has two marks, but one is an 'O', then pick a random spot"
                    # This logic is a bit unusual for a 'medium' difficulty, as it doesn't prioritize blocking.
                    elif ((N1 == 'X' and N2 == 'X' and N3 == 'O') or \
                          (N1 == 'X' and N2 == 'O' and N3 == 'X') or \
                          (N1 == 'O' and N2 == 'X' and N3 == 'X')): [cite: 114, 115]
                        while True:
                            num = random.randint(1, 6) [cite: 115, 116]

                            if num == 1 and N4 != 'X': [cite: 116]
                                robot_move = 4 [cite: 116]
                                break
                            elif num == 2 and N5 != 'X': [cite: 116, 117]
                                robot_move = 5 [cite: 117]
                                break
                            elif num == 3 and N6 != 'X': [cite: 117, 118]
                                robot_move = 6 [cite: 118]
                                break
                            elif num == 4 and N7 != 'X': [cite: 118, 119]
                                robot_move = 7 [cite: 119]
                                break
                            elif num == 5 and N8 != 'X': [cite: 119, 120]
                                robot_move = 8 [cite: 120]
                                break
                            elif num == 6 and N9 != 'X': [cite: 120, 121]
                                robot_move = 9 [cite: 121]
                                break

                    elif ((N4 == 'X' and N5 == 'X' and N6 == 'O') or \
                          (N4 == 'X' and N5 == 'O' and N6 == 'X') or \
                          (N4 == 'O' and N5 == 'X' and N6 == 'X')): [cite: 121, 122]
                        while True:
                            num = random.randint(1, 6) [cite: 122]

                            if num == 1 and N1 != 'X': [cite: 123]
                                robot_move = 1 [cite: 123]
                                break
                            elif num == 2 and N2 != 'X': [cite: 124]
                                robot_move = 2 [cite: 124]
                                break
                            elif num == 3 and N3 != 'X': [cite: 125]
                                robot_move = 3 [cite: 125]
                                break
                            elif num == 4 and N7 != 'X': [cite: 126]
                                robot_move = 7 [cite: 126]
                                break
                            elif num == 5 and N8 != 'X': [cite: 127]
                                robot_move = 8 [cite: 127]
                                break
                            elif num == 6 and N9 != 'X': [cite: 128]
                                robot_move = 9 [cite: 128]
                                break

                    elif ((N7 == 'X' and N8 == 'X' and N9 != 'O') or \
                          (N7 == 'X' and N8 == 'O' and N9 == 'X') or \
                          (N7 == 'O' and N8 == 'X' and N9 == 'X')): [cite: 129, 130, 131, 132, 133, 134, 135, 136]
                        while True:
                            num = random.randint(1, 6) [cite: 129]

                            if num == 1 and N1 != 'X': [cite: 130]
                                robot_move = 1 [cite: 130]
                                break
                            elif num == 2 and N2 != 'X': [cite: 131]
                                robot_move = 2 [cite: 131]
                                break
                            elif num == 3 and N3 != 'X': [cite: 132]
                                robot_move = 3 [cite: 132]
                                break
                            elif num == 4 and N4 != 'X': [cite: 133]
                                robot_move = 4 [cite: 133]
                                break [cite: 134]
                            elif num == 5 and N5 != 'X': [cite: 134]
                                robot_move = 5 [cite: 134]
                                break [cite: 135]
                            elif num == 6 and N6 != 'X': [cite: 135]
                                robot_move = 6 [cite: 135]
                                break [cite: 136]

                    elif ((N1 == 'X' and N4 == 'X' and N7 == 'O') or \
                          (N1 == 'X' and N4 == 'O' and N7 == 'X') or \
                          (N1 == 'O' and N4 == 'X' and N7 == 'X')): [cite: 136]
                        while True:
                            num = random.randint(1, 6) [cite: 137]

                            if num == 1 and N2 != 'X': [cite: 137]
                                robot_move = 2 [cite: 138]
                                break
                            elif num == 2 and N3 != 'X': [cite: 138, 139]
                                robot_move = 3 [cite: 139]
                                break
                            elif num == 3 and N4 != 'X': [cite: 139, 140]
                                robot_move = 4 [cite: 140]
                                break
                            elif num == 4 and N6 != 'X': [cite: 140, 141]
                                robot_move = 6 [cite: 141]
                                break
                            elif num == 5 and N7 != 'X': [cite: 141, 142]
                                robot_move = 7 [cite: 142]
                                break
                            elif num == 6 and N8 != 'X': [cite: 142, 143]
                                robot_move = 8 [cite: 143]
                                break

                    elif ((N3 == 'X' and N5 == 'X' and N7 == 'O') or \
                          (N3 == 'X' and N5 == 'O' and N7 == 'X') or \
                          (N3 == 'O' and N5 == 'X' and N7 == 'X')): [cite: 143, 144]
                        while True:
                            num = random.randint(1, 6) [cite: 144]

                            if num == 1 and N1 != 'X': [cite: 144, 145]
                                robot_move = 1 [cite: 145]
                                break
                            elif num == 2 and N2 != 'X': [cite: 145, 146]
                                robot_move = 2 [cite: 146]
                                break
                            elif num == 3 and N4 != 'X': [cite: 146, 147]
                                robot_move = 4 [cite: 147]
                                break
                            elif num == 4 and N6 != 'X': [cite: 147, 148]
                                robot_move = 6 [cite: 148]
                                break
                            elif num == 5 and N8 != 'X': [cite: 148, 149]
                                robot_move = 8 [cite: 149]
                                break
                            elif num == 6 and N9 != 'X': [cite: 149, 150]
                                robot_move = 9 [cite: 150]
                                break

                    # The following conditions (similar to easy difficulty) suggest picking a random spot
                    # in a row/column/diagonal where the player has at least one mark.
                    elif (N1 == 'X' or N2 == 'X' or N3 == 'X') and (N1 != 'X' or N2 != 'X' or N3 != 'X'): [cite: 150, 151]
                        robot_move = random.randint(1, 3) [cite: 151]
                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'): [cite: 151]
                        robot_move = random.randint(4, 6) [cite: 151]
                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'): [cite: 152]
                        robot_move = random.randint(7, 9) [cite: 152]
                    elif (N1 == 'X' or N5 == 'X' or N9 == 'X') and (N1 != 'X' or N5 != 'X' or N9 != 'X'): [cite: 152, 153]
                        num = random.randint(1, 3) [cite: 153]
                        if num == 1: [cite: 153]
                            robot_move = 1 [cite: 153]
                        elif num == 2: [cite: 153, 154]
                            robot_move = 5 [cite: 154]
                        else: [cite: 154]
                            robot_move = 9 [cite: 154]
                    elif (N3 == 'X' or N5 == 'X' or N7 == 'X') and (N3 != 'X' or N5 != 'X' or N7 != 'X'): [cite: 155]
                        num = random.randint(1, 3) [cite: 155]
                        if num == 1: [cite: 155, 156]
                            robot_move = 3 [cite: 156]
                        elif num == 2: [cite: 156]
                            robot_move = 5 [cite: 156]
                        else: [cite: 156, 157]
                            robot_move = 7 [cite: 157]
                    elif (N1 == 'X' or N4 == 'X' or N7 == 'X') and (N1 != 'X' or N4 != 'X' or N7 != 'X'): [cite: 157]
                        num = random.randint(1, 3) [cite: 157, 158]
                        if num == 1: [cite: 158]
                            robot_move = 1 [cite: 158]
                        elif num == 2: [cite: 158]
                            robot_move = 4 [cite: 158]
                        else: [cite: 159]
                            robot_move = 7 [cite: 159]
                    elif (N2 == 'X' or N5 == 'X' or N8 == 'X') and (N2 != 'X' or N5 != 'X' or N8 != 'X'): [cite: 159, 160]
                        num = random.randint(1, 3) [cite: 160]
                        if num == 1: [cite: 160]
                            robot_move = 2 [cite: 160]
                        elif num == 2: [cite: 161]
                            robot_move = 5 [cite: 161]
                        else: [cite: 161]
                            robot_move = 8 [cite: 161]
                    elif (N3 == 'X' or N6 == 'X' or N9 == 'X') and (N3 != 'X' or N6 != 'X' or N9 != 'X'): [cite: 162]
                        num = random.randint(1, 3) [cite: 162]
                        if num == 1: [cite: 162, 163]
                            robot_move = 3 [cite: 163]
                        elif num == 2: [cite: 163]
                            robot_move = 6 [cite: 163]
                        else: [cite: 164]
                            robot_move = 9 [cite: 164]
                    else: # If no specific condition met, choose a random empty spot
                        robot_move = random.randint(1, 9) [cite: 164]

                    # Update board with robot's move ('O')
                    if robot_move == N1 and N1 == 1: [cite: 165]
                        N1 = 'O' [cite: 165]
                        break [cite: 165]
                    elif robot_move == N2 and N2 == 2: [cite: 165, 166]
                        N2 = 'O' [cite: 166]
                        break [cite: 166]
                    elif robot_move == N3 and N3 == 3: [cite: 166]
                        N3 = 'O' [cite: 167]
                        break [cite: 167]
                    elif robot_move == N4 and N4 == 4: [cite: 167]
                        N4 = 'O' [cite: 167]
                        break [cite: 167]
                    elif robot_move == N5 and N5 == 5: [cite: 168]
                        N5 = 'O' [cite: 168]
                        break [cite: 168]
                    elif robot_move == N6 and N6 == 6: [cite: 168]
                        N6 = 'O' [cite: 169]
                        break [cite: 169]
                    elif robot_move == N7 and N7 == 7: [cite: 169]
                        N7 = 'O' [cite: 170]
                        break [cite: 170]
                    elif robot_move == N8 and N8 == 8: [cite: 170]
                        N8 = 'O' [cite: 170]
                        break [cite: 170]
                    elif robot_move == N9 and N9 == 9: [cite: 171]
                        N9 = 'O' [cite: 171]
                        break [cite: 171]

                print(f'\nRobot chose position {robot_move}') [cite: 171]
                time.sleep(3) # Pause for 3 seconds [cite: 172]

                os.system('cls')

                score_display = f'* Score *\nYou: {player_score}\nRobot: {robot_score}\n\n' [cite: 172]
                board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 173, 174]

                print(score_display) [cite: 172]
                print(board_layout) [cite: 173, 174]

                # Check for player win after robot's move
                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or \
                   (N4 == 'X' and N5 == 'X' and N6 == 'X') or \
                   (N7 == 'X' and N8 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N4 == 'X' and N7 == 'X') or \
                   (N2 == 'X' and N5 == 'X' and N8 == 'X') or \
                   (N3 == 'X' and N6 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N5 == 'X' and N9 == 'X') or \
                   (N3 == 'X' and N5 == 'X' and N7 == 'X'): [cite: 174, 175]
                    print('\n\n* Congratulations *\nYou won!') [cite: 175]
                    player_score += 1 [cite: 175]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 176]
                    while go_back != 1: [cite: 176]
                        go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 176]

                    break [cite: 177]

                # Check for robot win after robot's move
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or \
                   (N4 == 'O' and N5 == 'O' and N6 == 'O') or \
                   (N7 == 'O' and N8 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N4 == 'O' and N7 == 'O') or \
                   (N2 == 'O' and N5 == 'O' and N8 == 'O') or \
                   (N3 == 'O' and N6 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N5 == 'O' and N9 == 'O') or \
                   (N3 == 'O' and N5 == 'O' and N7 == 'O'): [cite: 177, 178]
                    print('\n\n* Too bad! *\nRobot won!') [cite: 178, 179]
                    robot_score += 1 [cite: 179]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 179]
                    while go_back != 1: [cite: 179, 180]
                        go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 180]

                    break [cite: 180]

                # Check for a tie after robot's move
                if N1 != 1 and N2 != 2 and N3 != 3 and \
                   N4 != 4 and N5 != 5 and N6 != 6 and \
                   N7 != 7 and N8 != 8 and N9 != 9: [cite: 180]
                    print('\nGame tied!') [cite: 181]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 181]
                    while go_back != 1: [cite: 181]
                        go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 181]

                    break [cite: 182]

    else:  # Hard difficulty
        player_score = 0
        robot_score = 0

        while True:
            os.system('cls')
            # Initialize board numbers
            N1, N2, N3 = 1, 2, 3
            N4, N5, N6 = 4, 5, 6
            N7, N8, N9 = 7, 8, 9 [cite: 182, 183]

            score_display = f'* Score *\nYou: {player_score}\nRobot: {robot_score}\n\n' [cite: 184]
            board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 184, 185, 186]

            print(score_display) [cite: 184]
            print(board_layout) [cite: 184, 185, 186]

            continue_game = int(input('\nStart game:\n1- Yes\n2- No\nR: ')) [cite: 186]
            while continue_game != 1 and continue_game != 2: [cite: 186]
                continue_game = int(input('\nInvalid option!\nStart game:\n1- Yes\n2- No\nR: ')) [cite: 186]

            if continue_game == 2: [cite: 187]
                break

            while True:
                while True:
                    os.system('cls')

                    score_display = f'* Score *\nYou: {player_score}\nRobot: {robot_score}\n\n' [cite: 188]
                    board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 189, 190]

                    print(score_display) [cite: 188]
                    print(board_layout) [cite: 189, 190]

                    player1_move = int(input('\nYour turn\nR: ')) [cite: 190]
                    while player1_move > 9 or player1_move < 1: [cite: 190]
                        player1_move = int(input('\nInvalid option! Enter a number from 1 to 9\nYour turn\nR: ')) [cite: 191]

                    # Update board with player's move ('X')
                    if player1_move == N1 and N1 == 1: [cite: 191]
                        N1 = 'X' [cite: 191]
                        break [cite: 192]
                    elif player1_move == N2 and N2 == 2: [cite: 192]
                        N2 = 'X' [cite: 192]
                        break [cite: 192]
                    elif player1_move == N3 and N3 == 3: [cite: 193]
                        N3 = 'X' [cite: 193]
                        break [cite: 193]
                    elif player1_move == N4 and N4 == 4: [cite: 193]
                        N4 = 'X' [cite: 194]
                        break [cite: 194]
                    elif player1_move == N5 and N5 == 5: [cite: 194]
                        N5 = 'X' [cite: 194]
                        break [cite: 195]
                    elif player1_move == N6 and N6 == 6: [cite: 195]
                        N6 = 'X' [cite: 195]
                        break [cite: 195]
                    elif player1_move == N7 and N7 == 7: [cite: 196]
                        N7 = 'X' [cite: 196]
                        break [cite: 196]
                    elif player1_move == N8 and N8 == 8: [cite: 196, 197]
                        N8 = 'X' [cite: 197]
                        break [cite: 197]
                    elif player1_move == N9 and N9 == 9: [cite: 197]
                        N9 = 'X' [cite: 198]
                        break [cite: 198]
                    else:
                        go_back = int(input('\nCannot select an already used position!\nEnter "1" to go back\nR: ')) [cite: 198]
                        while go_back != 1: [cite: 199]
                            go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 199]

                os.system('cls')

                score_display = f'* Score *\nYou: {player_score}\nRobot: {robot_score}\n\n' [cite: 199]
                board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 200, 201]

                print(score_display) [cite: 199]
                print(board_layout) [cite: 200, 201]

                # Check for player win
                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or \
                   (N4 == 'X' and N5 == 'X' and N6 == 'X') or \
                   (N7 == 'X' and N8 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N4 == 'X' and N7 == 'X') or \
                   (N2 == 'X' and N5 == 'X' and N8 == 'X') or \
                   (N3 == 'X' and N6 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N5 == 'X' and N9 == 'X') or \
                   (N3 == 'X' and N5 == 'X' and N7 == 'X'): [cite: 201, 202]
                    print('\n\n* Congratulations *\nYou won!') [cite: 202]
                    player_score += 1 [cite: 202]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 203]
                    while go_back != 1: [cite: 203]
                        go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 203]

                    break [cite: 204]

                # Check for robot win
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or \
                   (N4 == 'O' and N5 == 'O' and N6 == 'O') or \
                   (N7 == 'O' and N8 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N4 == 'O' and N7 == 'O') or \
                   (N2 == 'O' and N5 == 'O' and N8 == 'O') or \
                   (N3 == 'O' and N6 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N5 == 'O' and N9 == 'O') or \
                   (N3 == 'O' and N5 == 'O' and N7 == 'O'): [cite: 204, 205]
                    print('\n\n* Too bad! *\nRobot won!') [cite: 205, 206]
                    robot_score += 1 [cite: 206]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 206]
                    while go_back != 1: [cite: 206, 207]
                        go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 207]

                    break [cite: 207]

                # Check for a tie
                if N1 != 1 and N2 != 2 and N3 != 3 and \
                   N4 != 4 and N5 != 5 and N6 != 6 and \
                   N7 != 7 and N8 != 8 and N9 != 9: [cite: 207]
                    print('\nGame tied!') [cite: 208]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 208]
                    while go_back != 1: [cite: 208]
                        go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 208]

                    break [cite: 209]

                # Robot's turn (Hard difficulty - more complex AI logic)
                while True:
                    # Defensive moves (blocking player wins)
                    # Check for opponent having one mark and the rest are empty for the same line, prioritize center if available.
                    if (N1 == 'X' and N2 == 2 and N3 == 3 and N4 == 4 and N5 == 5 and N6 == 6 and N7 == 7 and N8 == 8 and N9 == 9) or \
                       (N1 == 1 and N2 == 2 and N3 == 'X' and N4 == 4 and N5 == 5 and N6 == 6 and N7 == 7 and N8 == 8 and N9 == 9) or \
                       (N1 == 1 and N2 == 2 and N3 == 3 and N4 == 4 and N5 == 5 and N6 == 6 and N7 == 'X' and N8 == 8 and N9 == 9) or \
                       (N1 == 1 and N2 == 2 and N3 == 3 and N4 == 4 and N5 == 5 and N6 == 6 and N7 == 7 and N8 == 8 and N9 == 'X'): [cite: 209, 210, 211]
                        robot_move = 5 [cite: 211] # Try to take the center

                    elif N1 == 'X' and N2 != 'X' and N3 != 'X' and N4 != 'X' and N5 != 'X' and N6 != 'X' and N7 != 'X' and N8 != 'X' and N9 == 'X': [cite: 211, 212]
                        num = random.randint(1, 4) [cite: 212]
                        if num == 1: [cite: 212, 213]
                            robot_move = 2 [cite: 213]
                        elif num == 2: [cite: 213]
                            robot_move = 4 [cite: 213]
                        elif num == 3: [cite: 213, 214]
                            robot_move = 6 [cite: 214]
                        elif num == 4: [cite: 214]
                            robot_move = 8 [cite: 214]

                    elif N1 != 'X' and N2 != 'X' and N3 == 'X' and N4 != 'X' and N5 != 'X' and N6 != 'X' and N7 == 'X' and N8 != 'X' and N9 != 'X': [cite: 215]
                        num = random.randint(1, 4) [cite: 215, 216]
                        if num == 1: [cite: 216]
                            robot_move = 2 [cite: 216]
                        elif num == 2: [cite: 216]
                            robot_move = 6 [cite: 216]
                        elif num == 3: [cite: 217]
                            robot_move = 4 [cite: 217]
                        elif num == 4: [cite: 217, 218]
                            robot_move = 8 [cite: 218]

                    # Specific corner/center related strategies
                    elif N5 == 'X' and N1 == 'X' and N3 == 3 and N7 == 7 and N9 == 9: [cite: 218, 219]
                        while True:
                            num = random.randint(1, 2) [cite: 219]
                            if num == 1: [cite: 219, 220]
                                robot_move = 3 [cite: 220]
                                break
                            elif num == 2: [cite: 220, 221]
                                robot_move = 7 [cite: 221]
                                break
                            else: [cite: 221]
                                break

                    elif N5 == 'X' and N1 == 1 and N3 == 'X' and N7 == 7 and N9 == 9: [cite: 222]
                        while True:
                            num = random.randint(1, 2) [cite: 223]
                            if num == 1: [cite: 223]
                                robot_move = 1 [cite: 223]
                                break [cite: 224]
                            elif num == 2: [cite: 224]
                                robot_move = 9 [cite: 224]
                                break [cite: 225]
                            else: [cite: 225]
                                break

                    elif N5 == 'X' and N1 == 1 and N3 == 3 and N7 == 'X' and N9 == 9: [cite: 225, 226]
                        while True:
                            num = random.randint(1, 2) [cite: 226]
                            if num == 1: [cite: 226, 227]
                                robot_move = 1 [cite: 227]
                                break
                            elif num == 2: [cite: 227, 228]
                                robot_move = 9 [cite: 228]
                                break

                    elif N5 == 'X' and N1 == 1 and N3 == 3 and N7 == 7 and N9 == 'X': [cite: 228, 229]
                        while True:
                            num = random.randint(1, 2) [cite: 229]
                            if num == 1: [cite: 229, 230]
                                robot_move = 3 [cite: 230]
                                break
                            elif num == 2: [cite: 230, 231]
                                robot_move = 7 [cite: 231]
                                break

                    elif N5 == 'X' and N1 == 1 and N3 == 3 and N7 == 7 and N9 == 9: [cite: 231, 232]
                        while True:
                            num = random.randint(1, 4) [cite: 232]
                            if num == 1: [cite: 232, 233]
                                robot_move = 1 [cite: 233]
                                break
                            elif num == 2: [cite: 233, 234]
                                robot_move = 3 [cite: 234]
                                break
                            elif num == 3: [cite: 234, 235]
                                robot_move = 7 [cite: 235]
                                break
                            elif num == 4: [cite: 235, 236]
                                robot_move = 9 [cite: 236]
                                break
                            else: [cite: 236]
                                break

                    # Blocking robot's potential wins (similar to medium difficulty but for 'O' marks)
                    elif ((N1 == 'O' and N2 == 'O' and N3 == 3) or \
                          (N1 == 'O' and N2 == 2 and N3 == 'O') or \
                          (N1 == 1 and N2 == 'O' and N3 == 'O') or \
                          (N4 == 4 and N5 == 'O' and N6 == 'O') or \
                          (N4 == 'O' and N5 == 5 and N6 == 'O') or \
                          (N4 == 'O' and N5 == 'O' and N6 == 6) or \
                          (N7 == 7 and N8 == 'O' and N9 == 'O') or \
                          (N7 == 'O' and N8 == 8 and N9 == 'O') or \
                          (N7 == 'O' and N8 == 'O' and N9 == 9)): [cite: 237, 238]
                        while True:
                            num = random.randint(1, 9) [cite: 239]
                            if num == 1 and N1 == 1 and N2 == 'O' and N3 == 'O': [cite: 239, 240]
                                robot_move = 1 [cite: 240]
                                break
                            elif num == 2 and N1 == 'O' and N2 == 2 and N3 == 'O': [cite: 240, 241]
                                robot_move = 2 [cite: 241]
                                break
                            elif num == 3 and N1 == 'O' and N2 == 'O' and N3 == 3: [cite: 241, 242]
                                robot_move = 3 [cite: 242]
                                break
                            elif num == 4 and N4 == 4 and N5 == 'O' and N6 == 'O': [cite: 242, 243]
                                robot_move = 4 [cite: 243]
                                break
                            elif num == 5 and N4 == 'O' and N5 == 5 and N6 == 'O': [cite: 243, 244]
                                robot_move = 5 [cite: 244]
                                break
                            elif num == 6 and N4 == 'O' and N5 == 'O' and N6 == 6: [cite: 245]
                                robot_move = 6 [cite: 245]
                                break
                            elif num == 7 and N7 == 7 and N8 == 'O' and N9 == 'O': [cite: 246]
                                robot_move = 7 [cite: 246]
                                break
                            elif num == 8 and N7 == 'O' and N8 == 8 and N9 == 'O': [cite: 247]
                                robot_move = 8 [cite: 247]
                                break
                            elif num == 9 and N7 == 'O' and N8 == 'O' and N9 == 9: [cite: 248]
                                robot_move = 9 [cite: 248]
                                break [cite: 249]
                            else: [cite: 249]
                                break

                    elif ((N1 == 'O' and N4 == 'O' and N7 == 7) or \
                          (N1 == 'O' and N4 == 4 and N7 == 'O') or \
                          (N1 == 1 and N4 == 'O' and N7 == 'O') or \
                          (N2 == 2 and N5 == 'O' and N8 == 'O') or \
                          (N2 == 'O' and N5 == 5 and N8 == 'O') or \
                          (N2 == 'O' and N5 == 'O' and N8 == 8) or \
                          (N3 == 3 and N6 == 'O' and N9 == 'O') or \
                          (N3 == 'O' and N6 == 6 and N9 == 'O') or \
                          (N3 == 'O' and N6 == 'O' and N9 == 9)): [cite: 250, 251]
                        while True:
                            num = random.randint(1, 9) [cite: 252]
                            if num == 1 and N1 == 1 and N4 == 'O' and N7 == 'O': [cite: 252]
                                robot_move = 1 [cite: 252]
                                break [cite: 253]
                            elif num == 2 and N2 == 2 and N5 == 'O' and N8 == 'O': [cite: 253]
                                robot_move = 2 [cite: 253]
                                break [cite: 254]
                            elif num == 3 and N3 == 3 and N6 == 'O' and N9 == 'O': [cite: 254]
                                robot_move = 3 [cite: 254]
                                break [cite: 255]
                            elif num == 4 and N1 == 'O' and N4 == 4 and N7 == 'O': [cite: 255, 256]
                                robot_move = 4 [cite: 256]
                                break
                            elif num == 5 and N2 == 'O' and N5 == 5 and N8 == 'O': [cite: 256, 257]
                                robot_move = 5 [cite: 257]
                                break
                            elif num == 6 and N3 == 'O' and N6 == 6 and N9 == 'O': [cite: 257, 258]
                                robot_move = 6 [cite: 258]
                                break
                            elif num == 7 and N1 == 'O' and N4 == 'O' and N7 == 7: [cite: 258, 259]
                                robot_move = 7 [cite: 259]
                                break
                            elif num == 8 and N2 == 'O' and N5 == 'O' and N8 == 8: [cite: 260]
                                robot_move = 8 [cite: 260]
                                break
                            elif num == 9 and N3 == 'O' and N6 == 'O' and N9 == 9: [cite: 261]
                                robot_move = 9 [cite: 261]
                                break
                            else: [cite: 262]
                                break

                    elif ((N1 == 'O' and N5 == 'O' and N9 == 9) or \
                          (N1 == 'O' and N5 == 5 and N9 == 'O') or \
                          (N1 == 1 and N5 == 'O' and N6 == 'O') or \
                          (N3 == 'O' and N5 == 'O' and N7 == 7) or \
                          (N3 == 'O' and N5 == 5 and N7 == 'O') or \
                          (N3 == 3 and N5 == 'O' and N7 == 'O')): [cite: 262, 263]
                        while True:
                            num = random.randint(1, 6) [cite: 263, 264]
                            if num == 1 and N1 == 1: [cite: 264]
                                robot_move = 1 [cite: 264]
                            elif num == 2 and N5 == 5: [cite: 264, 265]
                                robot_move = 5 [cite: 265]
                            elif num == 3 and N9 == 9: [cite: 265]
                                robot_move = 9 [cite: 265]
                            elif num == 4 and N3 == 3: [cite: 266]
                                robot_move = 3 [cite: 266]
                            elif num == 5 and N7 == 7: [cite: 266, 267]
                                robot_move = 7 [cite: 267]
                            else: [cite: 267]
                                break

                    # Blocking player's potential wins (similar to medium difficulty's blocking logic)
                    elif ((N1 == 'X' and N2 == 'X' and N3 != 'O') or \
                          (N1 == 'X' and N3 == 'X' and N2 != 'O') or \
                          (N2 == 'X' and N3 == 'X' and N1 != 'O')) and \
                         (N1 != 'X' or N2 != 'X' or N3 != 'X'): [cite: 268]
                        robot_move = random.randint(1, 3) [cite: 268]

                    elif ((N4 == 'X' and N5 == 'X' and N6 != 'O') or \
                          (N4 == 'X' and N6 == 'X' and N6 != 'O') or \
                          (N5 == 'X' and N6 == 'X' and N4 != 'O')) and \
                         (N4 != 'X' or N5 != 'X' or N6 != 'X'): [cite: 269]
                        robot_move = random.randint(4, 6) [cite: 269]

                    elif ((N7 == 'X' and N8 == 'X' and N9 != 'O') or \
                          (N7 == 'X' and N9 == 'X' and N8 != 'O') or \
                          (N8 == 'X' and N9 == 'X' and N7 != 'O')) and \
                         (N7 != 'X' or N8 != 'X' or N9 != 'X'): [cite: 270]
                        robot_move = random.randint(7, 9) [cite: 270]

                    elif ((N1 == 'X' and N4 == 'X' and N7 != 'O') or \
                          (N1 == 'X' and N7 == 'X' and N4 != 'O') or \
                          (N4 == 'X' and N7 == 'X' and N1 != 'O')) and \
                         (N1 != 'X' or N4 != 'X' or N7 != 'X'): [cite: 271]
                        while True:
                            num = random.randint(1, 3) [cite: 271]
                            if num == 1 and N1 != 'X': [cite: 272]
                                robot_move = 1 [cite: 272]
                                break
                            elif num == 2 and N4 != 'X': [cite: 273]
                                robot_move = 4 [cite: 273]
                                break
                            elif num == 3 and N7 != 'X': [cite: 274]
                                robot_move = 7 [cite: 274]
                                break
                            else: [cite: 275]
                                break

                    elif ((N2 == 'X' and N5 == 'X' and N8 != 'O') or \
                          (N2 == 'X' and N8 == 'X' and N5 != 'O') or \
                          (N5 == 'X' and N8 == 'X' and N2 != 'O')) and \
                         (N2 != 'X' or N5 != 'X' or N8 != 'X'): [cite: 275, 276]
                        while True:
                            num = random.randint(1, 3) [cite: 276]
                            if num == 1 and N2 != 'X': [cite: 277]
                                robot_move = 2 [cite: 277]
                                break
                            elif num == 2 and N5 != 'X': [cite: 278]
                                robot_move = 5 [cite: 278]
                                break
                            elif num == 3 and N8 != 'X': [cite: 279]
                                robot_move = 8 [cite: 279]
                                break
                            else: [cite: 280]
                                break

                    elif ((N3 == 'X' and N6 == 'X' and N9 != 'O') or \
                          (N3 == 'X' and N9 == 'X' and N6 != 'O') or \
                          (N6 == 'X' and N9 == 'X' and N3 != 'O')) and \
                         (N3 != 'X' or N6 != 'X' or N9 != 'X'): [cite: 280, 281]
                        while True:
                            num = random.randint(1, 3) [cite: 281]
                            if num == 1 and N3 != 'X': [cite: 281, 282]
                                robot_move = 3 [cite: 282]
                                break
                            elif num == 2 and N6 != 'X': [cite: 282, 283]
                                robot_move = 6 [cite: 283]
                                break
                            elif num == 3 and N9 != 'X': [cite: 283, 284]
                                robot_move = 9 [cite: 284]
                                break
                            else: [cite: 285]
                                break

                    elif ((N1 == 'X' and N5 == 'X' and N9 != 'O') or \
                          (N1 == 'X' and N9 == 'X' and N5 != 'O') or \
                          (N5 == 'X' and N9 == 'X' and N1 != 'O')) and \
                         (N1 != 'X' or N5 != 'X' or N9 != 'X'): [cite: 285, 286]
                        while True:
                            num = random.randint(1, 3) [cite: 286]
                            if num == 1 and N1 != 'X': [cite: 286, 287]
                                robot_move = 1 [cite: 287]
                                break
                            elif num == 2 and N5 != 'X': [cite: 287, 288]
                                robot_move = 5 [cite: 288]
                                break
                            elif num == 3 and N9 != 'X': [cite: 288, 289]
                                robot_move = 9 [cite: 289]
                                break
                            else: [cite: 289, 290]
                                break

                    elif ((N3 == 'X' and N5 == 'X' and N7 != 'O') or \
                          (N3 == 'X' and N7 == 'X' and N5 != 'O') or \
                          (N7 == 'X' and N5 == 'X' and N3 != 'O')) and \
                         (N3 != 'X' or N5 != 'X' or N7 != 'X'): [cite: 290, 291]
                        while True:
                            num = random.randint(1, 3) [cite: 291]
                            if num == 1 and N3 != 'X': [cite: 291, 292]
                                robot_move = 3 [cite: 292]
                                break
                            elif num == 2 and N5 != 'X': [cite: 292, 293]
                                robot_move = 5 [cite: 293]
                                break
                            elif num == 3 and N7 != 'X': [cite: 293, 294]
                                robot_move = 7 [cite: 294]
                                break
                            else: [cite: 294]
                                break

                    elif ((N1 == 'X' and N2 == 'X' and N3 == 'O') or \
                          (N1 == 'X' and N2 == 'O' and N3 == 'X') or \
                          (N1 == 'O' and N2 == 'X' and N3 == 'X')): [cite: 295]
                        while True:
                            num = random.randint(1, 6) [cite: 296]

                            if num == 1 and N4 != 'X': [cite: 296]
                                robot_move = 4 [cite: 296]
                                break [cite: 297]
                            elif num == 2 and N5 != 'X': [cite: 297]
                                robot_move = 5 [cite: 297]
                                break [cite: 298]
                            elif num == 3 and N6 != 'X': [cite: 298]
                                robot_move = 6 [cite: 298]
                                break [cite: 299]
                            elif num == 4 and N7 != 'X': [cite: 299]
                                robot_move = 7 [cite: 299]
                                break [cite: 300]
                            elif num == 5 and N8 != 'X': [cite: 300]
                                robot_move = 8 [cite: 300]
                                break [cite: 301]
                            elif num == 6 and N9 != 'X': [cite: 301]
                                robot_move = 9 [cite: 301]
                                break [cite: 302]
                            else: [cite: 302]
                                break

                    elif ((N4 == 'X' and N5 == 'X' and N6 == 'O') or \
                          (N4 == 'X' and N5 == 'O' and N6 == 'X') or \
                          (N4 == 'O' and N5 == 'X' and N6 == 'X')): [cite: 302, 303]
                        while True:
                            num = random.randint(1, 6) [cite: 303, 304]

                            if num == 1 and N1 != 'X': [cite: 304]
                                robot_move = 1 [cite: 304]
                                break
                            elif num == 2 and N2 != 'X': [cite: 305]
                                robot_move = 2 [cite: 305]
                                break
                            elif num == 3 and N3 != 'X': [cite: 306]
                                robot_move = 3 [cite: 306]
                                break
                            elif num == 4 and N7 != 'X': [cite: 307]
                                robot_move = 7 [cite: 307]
                                break
                            elif num == 5 and N8 != 'X': [cite: 308]
                                robot_move = 8 [cite: 308]
                                break
                            elif num == 6 and N9 != 'X': [cite: 309]
                                robot_move = 9 [cite: 309]
                                break
                            else: [cite: 310]
                                break

                    elif ((N7 == 'X' and N8 == 'X' and N9 != 'O') or \
                          (N7 == 'X' and N8 == 'O' and N9 == 'X') or \
                          (N7 == 'O' and N8 == 'X' and N9 == 'X')): [cite: 310, 311]
                        while True:
                            num = random.randint(1, 6) [cite: 311]

                            if num == 1 and N1 != 'X': [cite: 311, 312]
                                robot_move = 1 [cite: 312]
                                break
                            elif num == 2 and N2 != 'X': [cite: 312, 313]
                                robot_move = 2 [cite: 313]
                                break
                            elif num == 3 and N3 != 'X': [cite: 313, 314]
                                robot_move = 3 [cite: 314]
                                break
                            elif num == 4 and N4 != 'X': [cite: 314, 315]
                                robot_move = 4 [cite: 315]
                                break
                            elif num == 5 and N5 != 'X': [cite: 315, 316]
                                robot_move = 5 [cite: 316]
                                break
                            elif num == 6 and N6 != 'X': [cite: 316, 317]
                                robot_move = 6 [cite: 317]
                                break
                            else: [cite: 317, 318]
                                break

                    elif ((N1 == 'X' and N4 == 'X' and N7 == 'O') or \
                          (N1 == 'X' and N4 == 'O' and N7 == 'X') or \
                          (N1 == 'O' and N4 == 'X' and N7 == 'X')): [cite: 318, 319]
                        while True:
                            num = random.randint(1, 6) [cite: 319]

                            if num == 1 and N2 != 'X': [cite: 319, 320]
                                robot_move = 2 [cite: 320]
                                break
                            elif num == 2 and N3 != 'X': [cite: 320, 321]
                                robot_move = 3 [cite: 321]
                                break
                            elif num == 3 and N4 != 'X': [cite: 321, 322]
                                robot_move = 4 [cite: 322]
                                break
                            elif num == 4 and N6 != 'X': [cite: 322, 323]
                                robot_move = 6 [cite: 323]
                                break
                            elif num == 5 and N7 != 'X': [cite: 323, 324]
                                robot_move = 7 [cite: 324]
                                break
                            elif num == 6 and N8 != 'X': [cite: 324, 325]
                                robot_move = 8 [cite: 325]
                                break
                            else: [cite: 325, 326]
                                break

                    elif ((N3 == 'X' and N5 == 'X' and N7 == 'O') or \
                          (N3 == 'X' and N5 == 'O' and N7 == 'X') or \
                          (N3 == 'O' and N5 == 'X' and N7 == 'X')): [cite: 326]
                        while True:
                            num = random.randint(1, 6) [cite: 327]

                            if num == 1 and N1 != 'X': [cite: 327]
                                robot_move = 1 [cite: 327]
                                break [cite: 328]
                            elif num == 2 and N2 != 'X': [cite: 328]
                                robot_move = 2 [cite: 328]
                                break [cite: 329]
                            elif num == 3 and N4 != 'X': [cite: 329]
                                robot_move = 4 [cite: 329]
                                break [cite: 330]
                            elif num == 4 and N6 != 'X': [cite: 330]
                                robot_move = 6 [cite: 330]
                                break [cite: 331]
                            elif num == 5 and N8 != 'X': [cite: 331]
                                robot_move = 8 [cite: 331]
                                break [cite: 332]
                            elif num == 6 and N9 != 'X': [cite: 332]
                                robot_move = 9 [cite: 332]
                                break [cite: 333]
                            else: [cite: 333]
                                break

                    # Complex blocking/winning strategies (prioritizing forks or specific empty spots)
                    # These blocks are quite detailed and attempt to cover many board configurations.
                    elif ((N2 == 'X' and N6 == 'X' and N3 == 3 and N1 == 1 and N9 == 9) or \
                          (N2 == 'X' and N4 == 'X' and N1 == 1 and N7 == 7 and N3 == 3) or \
                          (N8 == 'X' and N4 == 'X' and N7 == 7 and N1 == 1 and N9 == 9) or \
                          (N8 == 'X' and N6 == 'X' and N7 == 7 and N3 == 3 and N9 == 9)): [cite: 334, 335]

                        num = random.randint(1, 3) [cite: 335]
                        if N2 == 'X' and N6 == 'X' and N3 == 3 and N1 == 1 and N9 == 9: [cite: 335]
                            if num == 1: [cite: 336]
                                robot_move = 1 [cite: 336]
                            elif num == 2: [cite: 336, 337]
                                robot_move = 3 [cite: 337] # Original code has == 3, should be = 3
                            else: [cite: 337]
                                robot_move = 7 [cite: 337] # Original code has == 7, should be = 7
                        elif N2 == 'X' and N4 == 'X' and N1 == 1 and N7 == 7 and N3 == 3: [cite: 338]
                            if num == 1: [cite: 338]
                                robot_move = 1 [cite: 338]
                            elif num == 2: [cite: 339]
                                robot_move = 3 [cite: 339] # Original code has == 3, should be = 3
                            else: [cite: 340]
                                robot_move = 9 [cite: 340] # Original code has == 9, should be = 9
                        elif N8 == 'X' and N4 == 'X' and N7 == 7 and N1 == 1 and N9 == 9: [cite: 340]
                            if num == 1: [cite: 341]
                                robot_move = 1 [cite: 341]
                            elif num == 2: [cite: 341, 342]
                                robot_move = 7 [cite: 342] # Original code has == 7, should be = 7
                            else: [cite: 342]
                                robot_move = 9 [cite: 342] # Original code has == 9, should be = 9
                        elif N8 == 'X' and N6 == 'X' and N7 == 7 and N3 == 3 and N9 == 9: [cite: 342, 343]
                            if num == 1: [cite: 343]
                                robot_move = 9 [cite: 343]
                            elif num == 2: [cite: 344]
                                robot_move = 3 [cite: 344] # Original code has == 3, should be = 3
                            else: [cite: 344]
                                robot_move = 7 [cite: 344] # Original code has == 7, should be = 7

                    # This block seems to try to pick a random available corner or side if other specific conditions aren't met
                    elif ((N1 == 1 and N2 == 'X' and N3 == 3) or \
                          (N2 == 'X' and N5 == 5 and N8 == 8) or \
                          (N1 == 1 and N4 == 'X' and N7 == 7) or \
                          (N4 == 'X' and N5 == 5 and N6 == 6) or \
                          (N2 == 2 and N5 == 5 and N8 == 'X') or \
                          (N7 == 7 and N8 == 'X' and N9 == 9) or \
                          (N4 == 4 and N5 == 5 and N6 == 'X') or \
                          (N3 == 3 and N6 == 'X' and N9 == 9)): [cite: 345, 346]
                        num = random.randint(1, 2) [cite: 346]
                        if N1 == 1 and N2 == 'X' and N3 == 3: [cite: 346]
                            if num == 1: [cite: 347]
                                robot_move = 1 [cite: 347]
                            else: [cite: 347, 348]
                                robot_move = 3 [cite: 348]
                        elif N2 == 'X' and N5 == 5 and N8 == 8: [cite: 348]
                            if num == 1: [cite: 349]
                                robot_move = 5 [cite: 349]
                            else: [cite: 349]
                                robot_move = 8 [cite: 349]
                        elif N1 == 1 and N4 == 'X' and N7 == 7: [cite: 350]
                            if num == 1: [cite: 350]
                                robot_move = 1 [cite: 350]
                            else: [cite: 351]
                                robot_move = 7 [cite: 351]
                        elif N4 == 'X' and N5 == 5 and N6 == 6: [cite: 351, 352]
                            if num == 1: [cite: 352]
                                robot_move = 5 [cite: 352]
                            else: [cite: 353]
                                robot_move = 6 [cite: 353]
                        elif N2 == 2 and N5 == 5 and N8 == 'X': [cite: 353]
                            if num == 1: [cite: 354]
                                robot_move = 2 [cite: 354]
                            else: [cite: 354]
                                robot_move = 5 [cite: 354]
                        elif N7 == 7 and N8 == 'X' and N9 == 9: [cite: 355]
                            if num == 1: [cite: 355]
                                robot_move = 7 [cite: 355]
                            else: [cite: 356]
                                robot_move = 9 [cite: 356]
                        elif N4 == 4 and N5 == 5 and N6 == 'X': [cite: 356]
                            if num == 1: [cite: 357]
                                robot_move = 4 [cite: 357]
                            else: [cite: 357]
                                robot_move = 5 [cite: 357]
                        elif N3 == 3 and N6 == 'X' and N9 == 9: [cite: 358]
                            if num == 1: [cite: 358]
                                robot_move = 3 [cite: 358]
                            else: [cite: 359]
                                robot_move = 9 [cite: 359]

                    # Remaining conditions are similar to Easy/Medium difficulty (random choice in a partially filled line)
                    elif (N1 == 'X' or N2 == 'X' or N3 == 'X') and (N1 != 'X' or N2 != 'X' or N3 != 'X'): [cite: 359, 360]
                        robot_move = random.randint(1, 3) [cite: 360]

                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'): [cite: 360, 361]
                        robot_move = random.randint(4, 6) [cite: 361]

                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'): [cite: 361]
                        robot_move = random.randint(7, 9) [cite: 361]

                    elif (N1 == 'X' or N5 == 'X' or N9 == 'X') and (N1 != 'X' or N5 != 'X' or N9 != 'X'): [cite: 362]
                        num = random.randint(1, 3) [cite: 362]
                        if num == 1: [cite: 362, 363]
                            robot_move = 1 [cite: 363]
                        elif num == 2: [cite: 363]
                            robot_move = 5 [cite: 363]
                        else: [cite: 363, 364]
                            robot_move = 9 [cite: 364]

                    elif (N3 == 'X' or N5 == 'X' or N7 == 'X') and (N3 != 'X' or N5 != 'X' or N7 != 'X'): [cite: 364]
                        num = random.randint(1, 3) [cite: 364, 365]
                        if num == 1: [cite: 365]
                            robot_move = 3 [cite: 365]
                        elif num == 2: [cite: 366]
                            robot_move = 5 [cite: 366]
                        else: [cite: 366, 367]
                            robot_move = 7 [cite: 367]

                    elif (N1 == 'X' or N4 == 'X' or N7 == 'X') and (N1 != 'X' or N4 != 'X' or N7 != 'X'): [cite: 367]
                        num = random.randint(1, 3) [cite: 367]
                        if num == 1: [cite: 367, 368]
                            robot_move = 1 [cite: 368]
                        elif num == 2: [cite: 368]
                            robot_move = 4 [cite: 368]
                        else: [cite: 368]
                            robot_move = 7 [cite: 368]

                    elif (N2 == 'X' or N5 == 'X' or N8 == 'X') and (N2 != 'X' or N5 != 'X' or N8 != 'X'): [cite: 369]
                        num = random.randint(1, 3) [cite: 369]
                        if num == 1: [cite: 369, 370]
                            robot_move = 2 [cite: 370]
                        elif num == 2: [cite: 370]
                            robot_move = 5 [cite: 370]
                        else: [cite: 371]
                            robot_move = 8 [cite: 371]

                    elif (N3 == 'X' or N6 == 'X' or N9 == 'X') and (N3 != 'X' or N6 != 'X' or N9 != 'X'): [cite: 371]
                        num = random.randint(1, 3) [cite: 372]
                        if num == 1: [cite: 372]
                            robot_move = 3 [cite: 372]
                        elif num == 2: [cite: 372, 373]
                            robot_move = 6 [cite: 373]
                        else: [cite: 373]
                            robot_move = 9 [cite: 373]
                    else: # If no specific condition met, choose a random empty spot
                        robot_move = random.randint(1, 9) [cite: 374]


                    # Update board with robot's move ('O')
                    if robot_move == N1 and N1 == 1: [cite: 374]
                        N1 = 'O' [cite: 374]
                        break [cite: 375]
                    elif robot_move == N2 and N2 == 2: [cite: 375]
                        N2 = 'O' [cite: 375]
                        break [cite: 375]
                    elif robot_move == N3 and N3 == 3: [cite: 375, 376]
                        N3 = 'O' [cite: 376]
                        break [cite: 376]
                    elif robot_move == N4 and N4 == 4: [cite: 376]
                        N4 = 'O' [cite: 376]
                        break [cite: 377]
                    elif robot_move == N5 and N5 == 5: [cite: 377]
                        N5 = 'O' [cite: 377]
                        break [cite: 378]
                    elif robot_move == N6 and N6 == 6: [cite: 378]
                        N6 = 'O' [cite: 378]
                        break
                    elif robot_move == N7 and N7 == 7: [cite: 378, 379]
                        N7 = 'O' [cite: 379]
                        break [cite: 379]
                    elif robot_move == N8 and N8 == 8: [cite: 379, 380]
                        N8 = 'O' [cite: 380]
                        break [cite: 380]
                    elif robot_move == N9 and N9 == 9: [cite: 380]
                        N9 = 'O' [cite: 381]
                        break [cite: 381]


                print(f'\nRobot chose position {robot_move}') [cite: 381]
                time.sleep(3) # Pause for 3 seconds [cite: 381]

                os.system('cls')

                score_display = f'* Score *\nYou: {player_score}\nRobot: {robot_score}\n\n' [cite: 382]
                board_layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  | {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n' [cite: 382, 383]

                print(score_display) [cite: 382]
                print(board_layout) [cite: 382, 383]

                # Check for player win after robot's move
                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or \
                   (N4 == 'X' and N5 == 'X' and N6 == 'X') or \
                   (N7 == 'X' and N8 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N4 == 'X' and N7 == 'X') or \
                   (N2 == 'X' and N5 == 'X' and N8 == 'X') or \
                   (N3 == 'X' and N6 == 'X' and N9 == 'X') or \
                   (N1 == 'X' and N5 == 'X' and N9 == 'X') or \
                   (N3 == 'X' and N5 == 'X' and N7 == 'X'): [cite: 383, 384]
                    print('\n\n* Congratulations *\nYou won!') [cite: 384]
                    player_score += 1 [cite: 384]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 385]
                    while go_back != 1: [cite: 385]
                        go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 385]

                    break [cite: 386]

                # Check for robot win after robot's move
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or \
                   (N4 == 'O' and N5 == 'O' and N6 == 'O') or \
                   (N7 == 'O' and N8 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N4 == 'O' and N7 == 'O') or \
                   (N2 == 'O' and N5 == 'O' and N8 == 'O') or \
                   (N3 == 'O' and N6 == 'O' and N9 == 'O') or \
                   (N1 == 'O' and N5 == 'O' and N9 == 'O') or \
                   (N3 == 'O' and N5 == 'O' and N7 == 'O'): [cite: 386, 387]
                    print('\n\n* Too bad! *\nRobot won!') [cite: 387, 388]
                    robot_score += 1 [cite: 388]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 388]
                    while go_back != 1: [cite: 388, 389]
                        go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 389]

                    break [cite: 389]

                # Check for a tie after robot's move
                if N1 != 1 and N2 != 2 and N3 != 3 and \
                   N4 != 4 and N5 != 5 and N6 != 6 and \
                   N7 != 7 and N8 != 8 and N9 != 9: [cite: 389]
                    print('\nGame tied!') [cite: 390]

                    go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 390]
                    while go_back != 1: [cite: 390]
                        go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 390]

                    break [cite: 391]

def Play_With_Friend():
    """
    Plays a game of Tic-Tac-Toe between two human players.
    """
    player1_score = 0
    player2_score = 0

    while True:
        os.system('cls')
        # Initialize board numbers
        N1, N2, N3 = 1, 2, 3
        N4, N5, N6 = 4, 5, 6
        N7, N8, N9 = 7, 8, 9 [cite: 391, 392]

        score_display = f'* Score *\nP1: {player1_score}\nP2: {player2_score}\n\n' [cite: 392]
        board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 393, 394]

        print(score_display) [cite: 392]
        print(board_layout) [cite: 393, 394]

        continue_game = int(input('\nStart game:\n1- Yes\n2- No\nR: ')) [cite: 394]
        while continue_game != 1 and continue_game != 2: [cite: 394]
            continue_game = int(input('\nInvalid option!\nStart game:\n1- Yes\n2- No\nR: ')) [cite: 394]

        if continue_game == 2: [cite: 395]
            break

        while True:
            while True:
                os.system('cls')

                score_display = f'* Score *\nP1: {player1_score}\nP2: {player2_score}\n\n' [cite: 395]
                board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 396, 397]

                print(score_display) [cite: 395]
                print(board_layout) [cite: 396, 397]

                player1_move = int(input('\nPlayer ONE turn\nR: ')) [cite: 397]
                while player1_move > 9 or player1_move < 1: [cite: 397]
                    player1_move = int(input('\nInvalid option! Enter a number from 1 to 9\nPlayer ONE turn\nR: ')) [cite: 398]

                # Update board with Player 1's move ('X')
                if player1_move == N1 and N1 == 1: [cite: 398]
                    N1 = 'X' [cite: 398]
                    break
                elif player1_move == N2 and N2 == 2: [cite: 398, 399]
                    N2 = 'X' [cite: 399]
                    break
                elif player1_move == N3 and N3 == 3: [cite: 399]
                    N3 = 'X' [cite: 399]
                    break [cite: 400]
                elif player1_move == N4 and N4 == 4: [cite: 400]
                    N4 = 'X' [cite: 400]
                    break
                elif player1_move == N5 and N5 == 5: [cite: 400, 401]
                    N5 = 'X' [cite: 401]
                    break
                elif player1_move == N6 and N6 == 6: [cite: 401]
                    N6 = 'X' [cite: 401]
                    break [cite: 402]
                elif player1_move == N7 and N7 == 7: [cite: 402]
                    N7 = 'X' [cite: 402]
                    break
                elif player1_move == N8 and N8 == 8: [cite: 402, 403]
                    N8 = 'X' [cite: 403]
                    break
                elif player1_move == N9 and N9 == 9: [cite: 403]
                    N9 = 'X' [cite: 403]
                    break
                else: # Invalid move
                    go_back = int(input('\nCannot select an already used position!\nEnter "1" to go back\nR: ')) [cite: 404]
                    while go_back != 1: [cite: 404]
                        go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 405]

            os.system('cls')

            score_display = f'* Score *\nP1: {player1_score}\nP2: {player2_score}\n\n' [cite: 405]
            board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 406, 407]

            print(score_display) [cite: 405]
            print(board_layout) [cite: 406, 407]

            # Check for Player 1 win
            if (N1 == 'X' and N2 == 'X' and N3 == 'X') or \
               (N4 == 'X' and N5 == 'X' and N6 == 'X') or \
               (N7 == 'X' and N8 == 'X' and N9 == 'X') or \
               (N1 == 'X' and N4 == 'X' and N7 == 'X') or \
               (N2 == 'X' and N5 == 'X' and N8 == 'X') or \
               (N3 == 'X' and N6 == 'X' and N9 == 'X') or \
               (N1 == 'X' and N5 == 'X' and N9 == 'X') or \
               (N3 == 'X' and N5 == 'X' and N7 == 'X'): [cite: 407, 408]
                print('\n\n* Congratulations *\nPlayer 1 won!') [cite: 408]
                player1_score += 1 [cite: 408]

                go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 409]
                while go_back != 1: [cite: 409]
                    go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 409]

                break

            # Check for Player 2 win (this check should ideally be after Player 2's turn)
            if (N1 == 'O' and N2 == 'O' and N3 == 'O') or \
               (N4 == 'O' and N5 == 'O' and N6 == 'O') or \
               (N7 == 'O' and N8 == 'O' and N9 == 'O') or \
               (N1 == 'O' and N4 == 'O' and N7 == 'O') or \
               (N2 == 'O' and N5 == 'O' and N8 == 'O') or \
               (N3 == 'O' and N6 == 'O' and N9 == 'O') or \
               (N1 == 'O' and N5 == 'O' and N9 == 'O') or \
               (N3 == 'O' and N5 == 'O' and N7 == 'O'): [cite: 410]
                print('\n\n* Congratulations *\nPlayer 2 won!') [cite: 411]
                player2_score += 1 [cite: 411]

                go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 411]
                while go_back != 1: [cite: 411, 412]
                    go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 412]

                break

            # Check for a tie
            if N1 != 1 and N2 != 2 and N3 != 3 and \
               N4 != 4 and N5 != 5 and N6 != 6 and \
               N7 != 7 and N8 != 8 and N9 != 9: [cite: 412]
                print('\nGame tied!') [cite: 412]

                go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 413]
                while go_back != 1: [cite: 413]
                    go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 413]

                break

            while True:
                player2_move = int(input('\nPlayer TWO turn\nR: ')) [cite: 414]
                while player2_move > 9 or player2_move < 1: [cite: 414]
                    player2_move = int(input('\nInvalid option! Enter a number from 1 to 9\nPlayer TWO turn\nR: ')) [cite: 415]

                # Update board with Player 2's move ('O')
                if player2_move == N1 and N1 == 1: [cite: 415]
                    N1 = 'O' [cite: 415]
                    break
                elif player2_move == N2 and N2 == 2: [cite: 416]
                    N2 = 'O' [cite: 416]
                    break
                elif player2_move == N3 and N3 == 3: [cite: 416]
                    N3 = 'O' [cite: 417]
                    break
                elif player2_move == N4 and N4 == 4: [cite: 417]
                    N4 = 'O' [cite: 417]
                    break
                elif player2_move == N5 and N5 == 5: [cite: 417, 418]
                    N5 = 'O' [cite: 418]
                    break
                elif player2_move == N6 and N6 == 6: [cite: 418]
                    N6 = 'O' [cite: 418]
                    break [cite: 419]
                elif player2_move == N7 and N7 == 7: [cite: 419]
                    N7 = 'O' [cite: 419]
                    break
                elif player2_move == N8 and N8 == 8: [cite: 419, 420]
                    N8 = 'O' [cite: 420]
                    break
                elif player2_move == N9 and N9 == 9: [cite: 420]
                    N9 = 'O' [cite: 420]
                    break [cite: 421]
                else: # Invalid move
                    go_back = int(input('\nCannot select an already used position!\nEnter "1" to go back\nR: ')) [cite: 421]
                    while go_back != 1: [cite: 421, 422]
                        go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 422]

            os.system('cls')

            score_display = f'* Score *\nP1: {player1_score}\nP2: {player2_score}\n\n' [cite: 422]
            board_layout = f' {N1}  | {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  | {N9} \n' [cite: 423, 424]

            print(score_display) [cite: 422]
            print(board_layout) [cite: 423, 424]

            # Check for Player 1 win (this check should ideally be after Player 1's turn)
            if (N1 == 'X' and N2 == 'X' and N3 == 'X') or \
               (N4 == 'X' and N5 == 'X' and N6 == 'X') or \
               (N7 == 'X' and N8 == 'X' and N9 == 'X') or \
               (N1 == 'X' and N4 == 'X' and N7 == 'X') or \
               (N2 == 'X' and N5 == 'X' and N8 == 'X') or \
               (N3 == 'X' and N6 == 'X' and N9 == 'X') or \
               (N1 == 'X' and N5 == 'X' and N9 == 'X') or \
               (N3 == 'X' and N5 == 'X' and N7 == 'X'): [cite: 424, 425]
                print('\n\n* Congratulations *\nPlayer 1 won!') [cite: 425]
                player1_score += 1 [cite: 425]

                go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 426]
                while go_back != 1: [cite: 426]
                    go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 426]

                break

            # Check for Player 2 win
            if (N1 == 'O' and N2 == 'O' and N3 == 'O') or \
               (N4 == 'O' and N5 == 'O' and N6 == 'O') or \
               (N7 == 'O' and N8 == 'O' and N9 == 'O') or \
               (N1 == 'O' and N4 == 'O' and N7 == 'O') or \
               (N2 == 'O' and N5 == 'O' and N8 == 'O') or \
               (N3 == 'O' and N6 == 'O' and N9 == 'O') or \
               (N1 == 'O' and N5 == 'O' and N9 == 'O') or \
               (N3 == 'O' and N5 == 'O' and N7 == 'O'): [cite: 427]
                print('\n\n* Congratulations *\nPlayer 2 won!') [cite: 428]
                player2_score += 1 [cite: 428]

                go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 428]
                while go_back != 1: [cite: 428, 429]
                    go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 429]

                break

            # Check for a tie
            if N1 != 1 and N2 != 2 and N3 != 3 and \
               N4 != 4 and N5 != 5 and N6 != 6 and \
               N7 != 7 and N8 != 8 and N9 != 9: [cite: 429]
                print('\nGame tied!') [cite: 429]

                go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 430]
                while go_back != 1: [cite: 430]
                    go_back = int(input('\nInvalid option!\nEnter "1" to go back\nR: ')) [cite: 430]

                break

def Main():
    """
    Main function to run the Tic-Tac-Toe game menu.
    """
    while True:
        os.system('cls')
        menu_choice = int(input('\n* Tic-Tac-Toe Menu *\n1- Play alone\n2- Play with a friend\n3- Exit\nR: ')) [cite: 431]

        if menu_choice == 3:
            print('\nProgram terminated!')
            break
        elif menu_choice == 1:
            os.system('cls')
            difficulty = int(input('\nSelect game difficulty\n1- Easy\n2- Medium\n3- Hard\nR: ')) [cite: 431, 432]
            while difficulty > 3 or difficulty < 1: [cite: 432]
                difficulty = int(input('\nInvalid value!\nSelect game difficulty\n1- Easy\n2- Medium\n3- Hard\nR: ')) [cite: 432]

            Play_Alone(difficulty)
            print('\nGame ended!')
            go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 432, 433]
            while go_back != 1: [cite: 433]
                go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 433]

        elif menu_choice == 2:
            os.system('cls')
            Play_With_Friend()
            print('\nGame ended!')
            go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 433, 434]
            while go_back != 1: [cite: 434]
                go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 434]

        else:
            os.system('cls')
            print('\nInvalid option!')

            go_back = int(input('\nEnter "1" to go back\nR: ')) [cite: 434, 435]
            while go_back != 1: [cite: 435]
                go_back = int(input('Invalid option!\nEnter "1" to go back\nR: ')) [cite: 435]

# Run the main menu
Main()