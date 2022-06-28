#! /usr/bin/env python3


# palindrome_function: this function will take in one list and one string as a parameter
# returning: print statements to console to inform user if the original_list is a palindrome
# or not a palindrome
# Note: A palindrome is a string that reads the same forwards and backwards.
def palindrome_function(original_list, user_string):
    # reversing the list
    reversed_list = original_list[::-1]

    # comparing reversed_list to original_list to
    # determine if the original_list is a palindrome
    if reversed_list == original_list:
        print("'" + user_string.lower() + "' is a palindrome.")
    else:
        print("'" + user_string.lower() + "' is not a palindrome!")


def main():
    # information msg
    print("enter 'exit' to end program")
    print()

    user_string = input("Enter string: ")
    user_list = list(user_string.lower())
    while user_string != 'exit':
        # putting our palindrome_function() to use
        palindrome_function(user_list, user_string)
        print()
        user_string = input("Enter string: ")
        # creating a variable called user_list
        # to hold the list and .lower() version
        # of user_string
        user_list = list(user_string.lower())

    print("Goodbye!")


if __name__ == "__main__":
    main()
