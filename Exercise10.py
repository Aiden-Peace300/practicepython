#! /usr/bin/env python3

import random   # used to generate random numbers


# finding_commonalities_function: this function will take in two list as a parameter
# returning: print statements to console to inform user of the elements that
# are similarly/commonalities with the two list pass in keep in mind. This
# function will not output duplicates.
def finding_commonalities_function(list1, list2):

    list3 = []
    for i in list1:
        for j in list2:
            if i == j:
                list3.append(i)

    print(list3)


# generating_list_function: this function will take in two list as a parameter
# returning: This will output nothing.
# goal: to create randomly generated numbers into the empty list(s) passed in
def generating_list_function():
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
