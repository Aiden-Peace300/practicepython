#! /usr/bin/env python3

"""
PROGRAMMER: Aiden Peace
DATE: 7/8/2022
TITLE: Exercise 11 - Check Primality Functions
DESCRIPTION: Ask the user for a number and determine
whether the number is prime or not. (For those who
have forgotten, a prime number is a number that has
no divisors.).
"""


# Ask the user for a number and determine
# whether the number is prime or not.
def are_you_an_even_digit(num):
    """
    FUNCTION DESCRIPTION:

    GOAL  : This function will determine
            if num is an even or odd number
    INPUT : This function will take in
            one number as a parameter.
    OUTPUT:  print statements to console to inform
             user if number passed in was even or odd.
    """

    if num % 2 == 0:
        print(str(num) + " is an even number")
    else:
        print(str(num) + " is an odd number")


def main():

    # promoting user for input
    print("Welcome to Odd or Even Program")
    print("Enter 'exit' at any time to exit program")
    user_num = input("Enter a number: ")

    # passing in user_num into our are_you_an_even_digit()
    if user_num != 'exit':
        are_you_an_even_digit(int(user_num))
        print()
    else:
        # if the user enters 'exit' than we will bid them fair well
        print("Goodbye")

    while user_num != 'exit':

        # prompting the user to enter input
        user_num = input("Enter a number: ")
        if user_num == 'exit':
            print("Goodbye")
        else:
            # passing in user_num into our are_you_an_even_digit()
            are_you_an_even_digit(int(user_num))
            print()


if __name__ == "__main__":
    main()
