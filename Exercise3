#! /urs/bin/env python3

import copy   # copy library enables us to use .copy() function


# less_than_five: this function will take in one list as a parameter
# returning: print statements to console to inform user of the elements that
# are less than five in given list
def less_than_five(list_holding_less_than_5_values):

    print("Here is a list of all the elements less than 5 in original list: ")
    for item in list_holding_less_than_5_values:
        if item < 5:
            print(item)

    print()


# print_list: is a function that takes in one list as an argument
# this function is meant to output all the elements in the list passed in.
# returning: printing elements to console
def print_list(list_of_nums):

    print("Here is a list of all the elements in original list:")
    for item in list_of_nums:
        print(item)

    print()


# less_than_given_num_function: this function will take in one list as a parameter
# returning: print statements to console to inform user of the elements that
# are less than given number in given list
def less_than_given_num_function(given_list, max_num):

    print("Here is a list of all the elements less than " + max_num + " in original list: ")
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
