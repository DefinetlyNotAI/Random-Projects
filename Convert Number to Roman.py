# Convert to roman
def fConvertRoman(nNo):
    try:
        nNo = int(nNo)
    except:
        return "--> error!"

    # opt out if number > 4999
    if nNo > 4999:
        return "--> out of range"

    # Create tuple
    tLetters = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))

    # temp str
    t = ""

    # cycle through, each time taking away highest no.
    for i in tLetters:

        while nNo >= i[0]:
            t += i[1]
            nNo -= i[0]
    return t


while True:
    print(fConvertRoman(input("Type Number here: ")))
