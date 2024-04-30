def has_equal_x_and_o(input_string):
    input_string = input_string.lower()
    if 'x' not in input_string and 'o' not in input_string:
        return False  # No X's or O's in the input string

    if input_string.count('x') == input_string.count('o'):
        return True
    else:
        return False

# Forever loop and basic input system with improved error checking
while True:
    input_string = input("Enter a string (or 'exit' to quit): ")
    if input_string.lower() == "exit":
        break
    if all(char in 'XxOo' for char in input_string):
        if has_equal_x_and_o(input_string):
            print("")
            print("The string has an equal number of X's and O's.")
            print("")
        else:
            print("")
            print("The string does not have an equal number of X's and O's.")
            print("")
    else:
        print("")
        print("Error: The input string should only contain X and O (No spaces, case insensitive).")
        print("")
 
