def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Forever loop and basic input system
while True:
    input_string = input("Enter a string (or 'exit' to quit): ")
    if input_string.lower() == "exit":
        break
    print(f"The number of vowels in the input string is: {count_vowels(input_string)}")
    
