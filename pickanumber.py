#comment


def guess(high,low):

    while True:
        guess = round((high + low)/2)

        print("my guess is ",guess)

        userinput = input("Is my guess high (h), low (l) or correct (c): ")

        if userinput == "h":
            high = guess
        elif userinput == "l":
            low = guess
        elif userinput == "c":
            print("I win!")
            break
        else:
            print("Your input sucks.")
    




def main():

    print("Pick a number between 1 and 10.")
    high = int(10)
    low = int(1)
    guess(high,low)

    return 0


main()