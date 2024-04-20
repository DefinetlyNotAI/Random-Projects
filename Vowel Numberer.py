# Function to vowels in a word
def fCharacter(sWord, sVowel):
    # Counter
    t = 0

    # For loop to find length of word
    for i in range(0, len(sWord)):

        if sWord[i] == sVowel:
            t += 1

    return sVowel + " " + str(t)


####################
def fVowel(sWord):
    a = fCharacter(sWord, "a")
    e = fCharacter(sWord, "e")
    i = fCharacter(sWord, "i")
    o = fCharacter(sWord, "o")
    u = fCharacter(sWord, "u")

    return a + "\n" + e + "\n" + i + "\n" + o + "\n" + u + "\n"

while True:
    print(fVowel(input("Input Word: ")))
