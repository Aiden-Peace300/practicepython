#! /urs/bin/env python3

import copy   # copy library enables us to use .copy() function

"""
PROGRAMMER: Aiden Peace
DATE: 6/24/2022
TITLE: Exercise 3 - List Less Than Ten
DESCRIPTION: Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the 
elements of the list that are less than 5.
Extras:
1. Instead of printing the elements one by one, 
make a new list that has all the elements less than 
5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that 
contains only elements from the original list a that 
are smaller than that number given by the user.
"""


def less_than_five(list_holding_less_than_5_values):
    """
    FUNCTION DESCRIPTION:

    GOAL  : This function will extract all
            elements less than 5 from the
            passed in list.
    INPUT : this function will take in
            one list as a parameter.
    OUTPUT: print statements to console to inform
            user of the elements that are less than
            five in given list.
    """

    print("Here is a list of all the elements less than 5 in original list: ")
    for item in list_holding_less_than_5_values:
        if item < 5:
            print(item)

    print()


def print_list(list_of_nums):
    """
    FUNCTION DESCRIPTION:

    GOAL  : This function will output all the
            elements in the list passed in.
    INPUT : This function will that takes in
            one list as an argument.
    OUTPUT: printing elements to console.
    """

    print("Here is a list of all the elements in original list:")
    for item in list_of_nums:
        print(item)

    print()


def less_than_given_num_function(given_list, max_num):
    """
    FUNCTION DESCRIPTION:

    GOAL  : This function will output all the
            elements in the list passed in that are
            less that users enters max number.
    INPUT : This function will take in
            one list as a parameter
    OUTPUT: print statements to console to inform
            user of the elements that are less
            than given number in given list
    """

    print("Here are all the elements less than " + max_num + " in original list: ")
    for item in given_list:
        if item < int(max_num):
            print(item)

    print()


def main():

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # getting users input
    users_max_num = input("Please enter a number: ")

    # creating shallow copy of 'a'
    list_holding_less_than_5_values = copy.copy(a)

    # putting functions to use
    print_list(a)
    less_than_five(list_holding_less_than_5_values)
    less_than_given_num_function(a, users_max_num)


'''
EASIER WAY (USEFUL WHEN THINKING IN BIG-O-NOTATION): 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for x in a:
    if x < 5:
        b.append(x)
print(b)
'''


if __name__ == "__main__":
    main()
