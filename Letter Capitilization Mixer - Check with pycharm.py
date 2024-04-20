def fAltWord(sWord):
    
    sNewWord = ""
    for i in range (0, len(sWord)):
        # Creating either a 0 (False) or 1 (True)
        if i%2:
            sNewWord = sNewWord + sWord[i].upper()
        else:
            sNewWord = sNewWord + sWord[i].lower()
            
    return sNewWord

while True:
    Text = input("Input Text: ")
    print(fAltWord(Text))

