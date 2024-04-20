while True:

    # Prog that takes given numbers and adds them together
    nTotal = 0
    nAmountNos = int(input("How many numbers?\n"))
    aNos = []

    for i in range(0, nAmountNos):
        nNo = int(input("Give me a number:"))
        nTotal += nNo
        aNos.append(nNo)

    # Now show user the highest number and the lowest number chosen
    aNos.sort()  # sort array
    print(str(aNos[0]) + " is the lowest. ")
    print(str(aNos[len(aNos) - 1]) + " is the highest.")
    print()
