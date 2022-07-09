#! /urs/bin/env python3

"""
PROGRAMMER: Aiden Peace
DATE: 6/24/2022
TITLE: Exercise 2 - Odd Or Even
DESCRIPTION: Ask the user for a number. Depending on whether
the number is even or odd, print out an appropriate message
to the user.

Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num)
   and one number to divide by (check). If check divides evenly into
   num, tell that to the user. If not, print a different appropriate
   message.
"""


def odd_or_even_function(num, check):
    """
    FUNCTION DESCRIPTION:

    GOAL  : This function will determine if
            the user entered an even, odd,
            or divisible by 4 number.
    INPUT : This function will take in one
            integer in as its parameter.
    OUTPUT: print statements to console to
            inform user if the numbered entered
            was an even, odd, or divisible by 4.
    """

    # Calculating when num will be even but not divisible by 4
    if int(num) % 2 == 0 and int(num) % 4 != 0:
        print("The number " + str(num) + " is an even number")

    # Calculating when num will be divisible by 4
    elif int(num) % 2 == 0 and int(num) % 4 == 0:
        print("The number " + str(num) + " is an number divisible by 4.")

    # Calculating when num will be odd
    else:
        print("The number " + str(num) + " is an odd number")

    # Calculating when num can or can't divide evenly into check
    if int(num) % int(check) == 0:
        print(str(num) + " divides evenly by " + str(check))
    else:
        print(str(num) + " does not divide evenly by " + str(check))


def main():
    # information msg
    print("enter 'exit' to end program")
    print()

    # user will be prompted to enter a number
    # this program will run until the user enters 'x'
    # then that will trigger the while loop
    # and program to close
    user_num = input("Enter a number: ")
    user_check = input("Enter a check number: ")
    while user_num != 'exit':
        odd_or_even_function(user_num, user_check)
        print()
        user_num = input("Enter a number: ")

    print("Goodbye!")


if __name__ == "__main__":
    main()
