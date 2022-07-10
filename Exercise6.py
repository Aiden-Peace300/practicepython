#! /usr/bin/env python3

"""
PROGRAMMER: Aiden Peace
DATE: 6/28/2022
TITLE: Exercise 6 - String Lists
DESCRIPTION: Ask the user for a string and print
out whether this string is a palindrome or not.
"""


def palindrome_function(user_string):
    """
    FUNCTION DESCRIPTION:

    GOAL  : This function will determine if a sting is a
            palindrome. A palindrome is a string that reads
            the same forwards and backwards.
    INPUT : This function will take in
            one string as a parameter.
    OUTPUT:  print statements to console to
             inform user if the original_list is a palindrome
             or not a palindrome
    """
    # 'original_list_no_whitespaces' is a list that
    # holds the same value as 'user_string' but with no
    # whitespaces and lower case
    original_list_no_whitespaces = []
    for ele in user_string.lower():
        if ele.strip():
            original_list_no_whitespaces.append(ele)

    # 'reversed_list' holds the reversed version of
    # 'original_list_no_whitespaces'
    reversed_list = original_list_no_whitespaces[::-1]

    # comparing reversed_list to original_list_no_whitespaces to
    # determine if the user_string is a palindrome
    if reversed_list == original_list_no_whitespaces:
        print("'" + user_string.lower() + "' is a palindrome.")
    else:
        print("'" + user_string.lower() + "' is not a palindrome!")


def main():
    # information msg
    print("enter 'exit' to end program")
    print()

    # prompting user for input
    user_string = input("Enter string: ")
    while user_string != 'exit':

        # putting our palindrome_function() to use
        palindrome_function(user_string)
        print()

        # prompting user for input
        user_string = input("Enter string: ")

    print("Goodbye!")


if __name__ == "__main__":
    main()
