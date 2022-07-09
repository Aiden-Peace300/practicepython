#! /urs/bin/env python3

"""
PROGRAMMER: Aiden Peace
DATE: 6/24/2022
TITLE: Exercise 1 : Guessing Game One
DESCRIPTION: Create a program that asks the user
to enter their name and their age. Print out a
message addressed to them that tells them the year
that they will turn 100 years old.
"""


def year_when_age_100_function(age):
    """
    FUNCTION DESCRIPTION:

    GOAL  : The goal of this function is
            to calculate when the user
            will turn 100 years old.
    INPUT : This function will take in one
            integer in as its parameter.
    OUTPUT: The output will be an integer
    """
    current_year = 2022
    year_when_age_100 = current_year - age + 100
    return year_when_age_100


def main():

    # prompting user to input their name and age
    user_name = input("Enter your name? ")
    user_age = int(input("Enter your age? "))

    # storing year_when_age_100_function() into a
    # variable called user_year_100
    user_year_100 = year_when_age_100_function(user_age)

    # outputting to console what year it will be when user turns 100 years old.
    print("Hello, " + user_name + " you will be 100 years old in the year " + str(user_year_100) + ".")


if __name__ == "__main__":
    main()
