#Write a function that returns the factorial of a given number.

#function to calculate factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)


#main program
def main():
    try:
        #take user input
        user_input = int(input("Enter a non-negative integer to calculate its factorial: "))

        if user_input < 0:
            print("Factorial is not defined for negative number. Please enter non negative number: ")
        else:
            result = factorial(user_input)

            print(f"the factorial of {user_input} is {result}.")

    except ValueError:
        print("Invalid input! please enter a valid integer.")

# Run the main function
if __name__ == "__main__":
    main()