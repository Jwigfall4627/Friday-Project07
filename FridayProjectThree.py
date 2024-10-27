import random
startOfGame = input ("Would you like to play a game?")
userStartOfGame = "Yes"



if startOfGame == userStartOfGame:
    print ("Welcome to my guessing game")
    computerGeneratedNumber = random.randint(1,10)
    print (computerGeneratedNumber)
    UserGeneratedNumber = int(input ("Please Enter a number"))
    while computerGeneratedNumber != UserGeneratedNumber:
        print ("Please Try again")
        print (computerGeneratedNumber)
        UserGeneratedNumber = int(input ("Please Enter a number"))
    print ("congrats")

else: "Pleaes try again next time"

