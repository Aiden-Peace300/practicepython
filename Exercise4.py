#! /usr/bin/env python3

"""
PROGRAMMER: Aiden Peace
DATE: 6/24/2022
TITLE: Exercise 4 - Divisors
DESCRIPTION: Create a program that asks the user
for a number and then prints out a list of all the
divisors of that number. (If you don’t know what a
divisor is, it is a number that divides evenly into
another number. For example, 13 is a divisor of 26
because 26 / 13 has no remainder.)
"""


def finding_divisor_function(num):
    """
    FUNCTION DESCRIPTION:

    GOAL  : This function will check each number
            in that range to see if it divides evenly
            into users entered number.
    INPUT : this function will take in
            one number as a parameter.
    OUTPUT: Print statements to console to inform
            user of every number that evenly divides 
            into the number that the user entered.
    """
    
    divisor_list = []  # Creating an empty list

    # from 1 though num we will check each number
    # in that range to see if it divides evenly
    # into users entered number.
    for item in list(range(1, num + 1)):
        if num % item == 0:
            divisor_list.append(item)

    # outputting to the console divisor_list with tabs
    print("\t", divisor_list)


def main():

    # prompting the user to enter input
    user_num = int(input("Enter a number: "))

    # outputting to the console the list for all the possible divisors for entered number
    print("List of all the divisors for the number " + str(user_num) + ":")
    finding_divisor_function(user_num)


if __name__ == "__main__":
    main()
