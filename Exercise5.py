#! /usr/bin/env python3

import random   # used to generate random numbers


# finding_commonalities_function: this function will take in two list as a parameter
# returning: print statements to console to inform user of the elements that
# are similarly/commonalities with the two list pass in keep in mind. This
# function will not output duplicates.
def finding_commonalities_function(list1, list2):

    # closer look:
    # intersection() allows arbitrary number of arguments (sets).
    # set() method is used to convert any of the iterable to sequence of
    # iterable elements with distinct elements, commonly called Set.
    # The list() function creates a list object.
    print(set(list1).intersection(list2))


# generating_list_function: this function will take in two list as a parameter
# returning: This will output nothing.
# goal: to create put randomly generated numbers into the empty list passed in
def generating_list_function(list1, list2):
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
