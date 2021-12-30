import random




def playersChoose(people):
#Give each player a 1 or 2.
    
    for i in people:
        print(people)
        if people[i] != 3:
            randomNumber = random.randint(0,1)
            print("The random number is ",randomNumber)
            people[i] = randomNumber
    print(people)
    return people

def eliminateLosers(people):
    for i in people:
        if people[i] == 1:
            people[i] ==3


def main():
    people = [
        1,
        2,
        8,
        4,
        5,
        6,
        7,
        1,
        1,
        1
    ]

    while True:

        #Players choose heads or tails.
        people = playersChoose(people)

        #Flip the coin.    
        coin = random.randint(0,1)

        #Eliminate losers.
        people = eliminateLosers(people)



main()