# Convert to roman
def fConvertRoman(sNo):
    # Create tuple
    tLetters = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))

    # temp number
    nResult = 0

    #
    nStartPos = 0

    # cycle through, looking for a letter from tuple.
    for number, letter in tLetters:

        # print(number, letter)
        while sNo[nStartPos:nStartPos + len(letter)] == letter:
            nResult += number
            nStartPos += len(letter)

    return nResult


while True:
    print(fConvertRoman(input("Type Roman Number: ")))
