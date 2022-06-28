#! /usr/bin/env python3


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
    print(list(set(list1).intersection(list2)))


def main():

    # Given list
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # outputting given list(s) to console
    print("Given List:")
    print(a)
    print(b)
    print()

    # outputting commonalities and using finding_commonalities_function()
    print("Commonalities between the two list w/ no duplicates: ")
    finding_commonalities_function(a, b)


if __name__ == "__main__":
    main()
