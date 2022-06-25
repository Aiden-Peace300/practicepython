#! /usr/bin/env python3


def finding_divisor_function(num):
    
    divisor_list = []  # Creating an empty list

    # from 1 though num we will check each number
    # in that range to see if it divides evenly
    # into users entered number.
    for item in list(range(1, num + 1)):
        if num % item == 0:
            divisor_list.append(item)

    # outputting to the console divisor_list with tabs
    print("\t", divisor_list)


def main():

    # prompting the user to enter input
    user_num = int(input("Enter a number: "))

    # outputting to the console the list for all the possible divisors for entered number
    print("List of all the divisors for the number " + str(user_num) + ":")
    finding_divisor_function(user_num)


if __name__ == "__main__":
    main()
