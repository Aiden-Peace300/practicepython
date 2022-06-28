#! /usr/bin/env python3

# EXERCISE 7 : Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements 
# of this list in it.
def main():
    # Given list
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    even_list = [i for i in a if i % 2 == 0]

    '''
    'even_list' is just like the logic below *just in one line*:

    even_list = []
    for i in a:
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)
    '''

    print("Given list:")
    print(a)

    print()

    print("List of all the even digits in list 'a': ")
    print(even_list)


if __name__ == "__main__":
    main()
