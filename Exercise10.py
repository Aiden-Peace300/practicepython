#! /usr/bin/env python3

import random   # used to generate random numbers

"""
PROGRAMMER: Aiden Peace 
DATE: 7/6/2022
TITLE: Exercise 10 : List Overlap Comprehensions
DESCRIPTION: This week’s exercise is going to be revisiting an 
old exercise (see Exercise 5), except require the solution in 
a different way. Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  
and write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
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
    list3 = []
    for i in list1:
        for j in list2:
            if i == j:
                list3.append(i)

    print(list3)


def generating_list_function():
    """
    FUNCTION DESCRIPTION:

    GOAL  : This function will find commonalities with no duplicates
            and return these values to console.
    INPUT : This function will take in
            two list as a parameter (preferable empty lists)
    OUTPUT:  This will output nothing.
    """

    list1 = random.sample(range(1, 30), 12)
    list2 = random.sample(range(1, 30), 16)
    return list1, list2


def main():

    # using generating_list_function()
    list1, list2 = generating_list_function()

    # outputting given list(s) to console
    print("Random generated List:")
    print(list1)
    print(list2)
    print()

    # outputting commonalities and using finding_commonalities_function()
    print("Commonalities between the two list w/ no duplicates: ")
    finding_commonalities_function(list1, list2)


if __name__ == "__main__":
    main()
