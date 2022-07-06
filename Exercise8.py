#! /usr/bin/env python3
# EXERCISE 8: Rock Paper Scissors program


def main():

    # welcome and rules output to console for players understanding
    print("Welcome to Aiden's Rock-Paper-Scissors Game")
    print("Rules: Type out the word \"Rock\", \"Paper\", \"Scissors\" to play that decision - X - Exit")
    print()     # print statement for spacing

    # taking players name and saving it in a variable for later usage
    player1_name = input("Player 1: Enter your name: ").capitalize()
    player2_name = input("Player 2: Enter your name: ").capitalize()
    print()     # print statement for spacing

    # variable list:
    game_list = ["Rock", "Paper", "Scissors"]
    status = True
    rounds = 0
    player1_score = 0
    player2_score = 0

    while status or rounds < 3:

        # taking players playing decision
        player1 = input(player1_name + " enter your play: ").capitalize()
        player2 = input(player2_name + " enter your play: ").capitalize()

        # if the players enter the same thing we will output
        # "Tie" and the rounds will not be incremented.
        if player1 == player2:
            if player1 != 'X' and player2 != 'X':
                print('Tie')
        # Rock beats scissors : if the player uses rock to beat
        # Scissors then the program will output the winner of the round
        # and give them a point
        elif player1 == game_list[0] and player2 == game_list[2]:
            print("Rock Wins - " + player1_name + " earns a point")
            print()
            player1_score += 1
            rounds += 1
        elif player2 == game_list[0] and player1 == game_list[2]:
            print("Rock Wins - " + player2_name + " earns a point")
            print()
            player2_score += 1
            rounds += 1
        # Scissor beats paper : if the player uses scissors to beat
        # paper then the program will output the winner of the round
        # and give them a point
        elif player1 == game_list[2] and player2 == game_list[1]:
            print("Scissor Wins - " + player1_name + " earns a point")
            print()
            player1_score += 1
            rounds += 1
        elif player2 == game_list[2] and player1 == game_list[1]:
            print("Scissor Wins - " + player2_name + " earns a point")
            print()
            player2_score += 1
            rounds += 1
        # Paper beats rock : if the player uses paper to beat
        # rock then the program will output the winner of the round
        # and give them a point
        elif player1 == game_list[1] and player2 == game_list[0]:
            print("Paper Wins - " + player1_name + " earns a point")
            print()
            player1_score += 1
            rounds += 1
        elif player2 == game_list[1] and player1 == game_list[0]:
            print("Paper Wins - " + player2_name + " earns a point")
            print()
            player2_score += 1
            rounds += 1

        # when a player or both players press 'X'
        # we will tell them goodbye and then exit program
        if player1 == 'X' and player2 == 'X':
            print("Both of you are quitters... what a shame")
            status = False
        elif player1 == 'X':
            print(player1_name + " Doesn't want to play anymore Goodbye")
            status = False
        elif player2 == 'X':
            print(player2_name + " Doesn't want to play anymore Goodbye")
            status = False

        # when we are complete with round 3 the game is over
        # we will then output the winner of the game and as
        # the players if they would like to play again
        if rounds == 3:
            if player1_score <= 3 and player2_score <= 2:
                print(player1_name + " Has won this game")
            elif player2_score <= 3 and player1_score <= 2:
                print(player2_name + " Has won this game")
            else:
                print("Something is wrong please tell Programmer what's going on")
            print()
            check = input("Would you like to play again? Y/N: ").capitalize()
            if check == 'Y':
                rounds = 0
                continue
            else:
                print("Goodbye")
                status = False


if __name__ == "__main__":
    main()
