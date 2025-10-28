#!/usr/bin/env python3
# Created by: Shem
# Created on: 10/27/2025
# This program checks if you are allowed to date grandparents' grandchild
# based on your age. It handles invalid input safely.

# Constants for age boundaries
import const


def main():
    # Ask the user to enter their age
    user_input = input("Enter your age: ")

    try:
        # Try to convert input to integer
        age = int(user_input)

        # Check if age is within allowed boundaries using AND
        if age >= const.MIN_AGE and age <= const.MAX_AGE:
            print("You are allowed to date their grandchild!")
        else:
            print("Sorry, your age does not meet the grandparents' criteria.")

    except ValueError:
        # Handle invalid input
        print(user_input, "is not a valid number.")


# This ensures the program starts
if __name__ == "__main__":
    main()
