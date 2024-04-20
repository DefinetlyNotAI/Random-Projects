# Here's the word to turn to uppercase
while True:
    sName = input("What is your name? ")

    sName = sName[0].upper() + sName[1:len(sName)].lower()

    print(sName)

