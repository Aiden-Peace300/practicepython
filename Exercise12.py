#! /usr/bin/env python3

import random as rand

"""
PROGRAMMER: Aiden Peace
DATE: 7/10/2022
TITLE: Exercise 12 - List Ends
DESCRIPTION: Write a program that takes a list 
of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last 
elements of the given list. For practice, write 
this code inside a function.
"""


def new_list_only_extracting_first_and_last_element(og_list, new_list):
    """
    FUNCTION DESCRIPTION:

    GOAL  : This function will append
            first and last element of the og_list
    INPUT : This function will take in
            two list as a parameter.
    OUTPUT: Nothing.
    """

    # storing the length of og_list in 'og_length'
    og_length = len(og_list)

    # appending the first element of 'og_list' into 'new_list'.
    new_list.append(og_list[0])

    # appending the very last element of 'og_list'
    # regardless of its length into 'new_list'
    new_list.append(og_list[og_length - 1])

    # printing 'new_list'
    print(new_list)


def main():

    # Storing generated random numbers in a list called 'random_list'
    random_list = rand.sample(range(10, 30), 16)

    # printing our original list to console
    print("Here is your original list: ")
    print(random_list)
    print()

    # creating an empty list
    new_list = []

    # using our new_list_only_extracting_first_and_last_element()
    # and passing in 'random_list' and 'new_list' into this function.
    print("Here is your new list with only the first and last elements of the original list: ")
    new_list_only_extracting_first_and_last_element(random_list, new_list)


if __name__ == "__main__":
    main()
