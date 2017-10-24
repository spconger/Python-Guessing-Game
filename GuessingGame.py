#this program will implement
# a guessing game in which the user
# gets 10 chances to guess a number
# between one and 1000
# A players is scored by the number of guesses
# it takes. Each wrong guess subtracts one point
# a player can play the game many times
# and the program will return the average score
# across those games.

#import random function
from random import randrange

#Introduce the game
def intro():
    print("*******************************************")
    print ("The game will choose a random number ")
    print ("between 1 and 1000. You will be given ")
    print("10 guesses. You start with 10 Points. Each")
    print("wrong guess subracts a point. You can play")
    print("As many times as you like")
    print("*******************************************")

#get the users name
def getName():
    name=input("Enter your player name")
    return name

#Set the random number
def getRandom():
    number = randrange(1,1001)
    return number

#Get the user's guess
def getGuess():
    guess=int(input("Enter your guess: "))
    return guess

#determine if the quess is high or low or correct            
def evaluateGuess(number, guess):
    state=0 #used so we can break loop if correct
    if guess > number:
        print ("Your guess is too large")
    elif guess < number:
        print ("your guess is too low")
    else:
        print("Congratualations! you got it")
        state = 1 
    return state

def play():
    number=getRandom() #call getRandom
    #print (number) #for testing
    score=10 #beginning score
    for i in range (0,11): #10 tries
        guess=getGuess() # call guess
        state = evaluateGuess(number, guess) #evaluate guess
        if state==1: #if answer was correct break loop
            break
        score = score - 1 #if not correct subtract one
    return score 

# this is the main function
#that calls most of the rest
def game():
    choice='y' #set the value for the while 
    scores=[] #initialize the list for scores
    while choice=='y': #start loop
        score=play() #Call play
        print ("Your score was",score) #print current score
        scores.append(score) #add to list
        choice = input("Do your want to play again? y to continue: ")
        choice.lower() #make sure its a lower case y
        
    return scores   

#average the scoeres
def getAverageScore(scores):
    total=0
    for item in scores:
        total += item
    average = total/len(scores)
    return average

#print the average
def printAverage(average, name):
     print (name,", Your average score is",average)

def main():
    intro() #call intro
    name=getName() #get the players name
    scores=game() #begin the game
    average=getAverageScore(scores) #all done, average scores
    printAverage(average,name) #print average      
    

main()
