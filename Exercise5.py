#! /usr/bin/env python3

import random   # used to generate random numbers

"""
PROGRAMMER: Aiden Peace
DATE: 6/27/2022
TITLE: Exercise 4 - Divisors
DESCRIPTION: Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  
And write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:
Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""


def finding_commonalities_function(list1, list2):
    """
    FUNCTION DESCRIPTION:

    GOAL  : This function will find commonalities with no duplicates
            and return these values to console.
    INPUT : This function will take in
            two list as a parameter.
    OUTPUT:  print statements to console to inform user of the elements that
             are similarly/commonalities with the two list pass in keep in mind. This
             function will not output duplicates.
    """
    # closer look:
    # intersection() allows arbitrary number of arguments (sets).
    # set() method is used to convert any of the iterable to sequence of
    # iterable elements with distinct elements, commonly called Set.
    # The list() function creates a list object.
    print(set(list1).intersection(list2))


# generating_list_function: this function will take in two list as a parameter
# returning: This will output nothing.
# goal: to create randomly generated numbers into the empty list(s) passed in
def generating_list_function(list1, list2):
    """
    FUNCTION DESCRIPTION:

    GOAL  : This function will find commonalities with no duplicates
            and return these values to console.
    INPUT : This function will take in
            two list as a parameter (preferable empty lists)
    OUTPUT:  This will output nothing.
    """

    for i in range(0, 11):
        n = random.randint(1, 100)
        list1.append(n)

    for i in range(0, 13):
        n = random.randint(1, 100)
        list2.append(n)


def main():

    # Creating/generating random list
    random_list1 = []
    random_list2 = []

    # using generating_list_function()
    generating_list_function(random_list1, random_list2)

    # outputting given list(s) to console
    print("Random generated List:")
    print(random_list1)
    print(random_list2)
    print()

    # outputting commonalities and using finding_commonalities_function()
    print("Commonalities between the two list w/ no duplicates: ")
    finding_commonalities_function(random_list1, random_list2)


if __name__ == "__main__":
    main()
