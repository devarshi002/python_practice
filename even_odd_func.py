#Create a function that checks if a number is even or odd.

def is_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
#main program

def main():
    #take user input
    try:
        user_input = int(input("Enter a number: "))

        #call the function with the user input
        result = is_even(user_input)

        #display the result
        print(f"the number {user_input} is {result}.")
    
    except ValueError:
        print("Invalid input! please enter an integer.")


#Run the main function

if __name__ == "__main__":
    main()