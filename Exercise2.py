#! /urs/bin/env python3

# odd_or_even_function: this function will take in one integer parameter
# returning: print statements to console to inform user if the numbered entered
# was an even, odd, or divisible by 4.
def odd_or_even_function(num, check):

    # Calculating and outputting when num will be even but not divisible by 4
    if int(num) % 2 == 0 and int(num) % 4 != 0:
        print("The number " + str(num) + " is an even number")

    # Calculating and outputting when num will be divisible by 4
    elif int(num) % 2 == 0 and int(num) % 4 == 0:
        print("The number " + str(num) + " is an number divisible by 4.")

    # Outputting when num will be odd
    else:
        print("The number " + str(num) + " is an odd number")

    # Calculating and outputting when num can or can't divide evenly into check
    if int(num) % int(check) == 0:
        print(str(num) + " divides evenly by " + str(check))
    else:
        print(str(num) + " does not divide evenly by " + str(check))


def main():
    # information msg
    print("enter 'exit' to end program")
    print()

    # user will be prompted to enter a number
    # this function will run until the user enters 'x'
    # then that will trigger the while loop to close
    user_num = input("Enter a number: ")
    user_check = input("Enter a check number: ")
    while user_num != 'exit':
        odd_or_even_function(user_num, user_check)
        print()
        user_num = input("Enter a number: ")

    print("¡Hasta luego amigo!")


if __name__ == "__main__":
    main()