#! /usr/bin/env python3
# importing the random module
import random

# Exercise 9 : Guessing Game One


def main():

    # generating a random number for future usage
    random_number = random.randrange(1, 10)

    # taking in users guess for future usage
    print("Welcome to Aiden's Guessing Random Number Game\nPlease enter 'exit' when you are ready to exit")
    users_guess = input("Enter a number from 1-9: ")

    while users_guess.lower != 'exit':
        if int(random_number) == int(users_guess):
            # if the user and the randomly generated number do match
            # we will let the user know they are correct and ask them
            # to play again until they enter 'exit'
            print("You guessed the number correctly!")
            print("Random number was: " + str(random_number))
            print("your number was: " + str(users_guess))
            print()
            random_number = random.randrange(1, 10)
            users_guess = input("Enter a number from 1-9: ")
        else:
            # if the user and the randomly generated number do not match
            # we will tell the user if their guess was too high or too low 
            # and ask them to guess again until their guess and 
            # random_number are equivalent
            print("You guessed the number incorrectly!")
            if int(users_guess) < int(random_number):
                print("Your guess was too low. Try again")
            elif int(users_guess) > int(random_number):
                print("Your guess was too high. Try again")
            users_guess = input("Enter a number from 1-9: ")

    # if user_guess == 'exit' we will
    # tell the user goodbye
    print("Goodbye")


if __name__ == "__main__":
    main()
