## GUESS THE NUMBER ##

import random #To import the random module to perform random actions

random_number = (random.randint(1,80)) #To generate a random number between 1 to 80

print("Guess the number between 1 to 80 !!!")

#while loop runs until the correct number is guessed by player
while True:
    guess = int(input("Enter your guess:")) #To get the input as integer

    if guess>random_number: # If player guess is higher than the system generated number
        print("Too High.Try again")
    elif guess<random_number:  # If player guess is lower than the system generated number
        print("Too low.Try again")
    else:
        print("Congratulations your guess is correct \n") # If player guessed the correct number same as system generated
        break #exits the loop


## UNSCRAMBLE THE JUMBLED WORD ##

import random #To import the random module to perform random actions

words=["python","java","javascript","automation","pytest","guvi","selenium"]
random_word = random.choice(words) #To randomly choose a word from the words list

s_list=list(random_word) #This converts the selected word to list like ['j','a','v','a']
random.shuffle(s_list) #Shuffle the letters ['a','j','v','a']

print("Unscramble the jumbled word !!! \n",s_list)

#Loop runs until player types the correct word
while True:
    guess=input("Enter your guess:") # To get the input as a string

#To check if the player's string matches the word in the list
    if guess.lower()!=random_word: #the player's input is converted to lowercase even if the user types it in uppercase
        print("Incorrect!!Try again")
    else:
        print("Congrats!!! You found the correct word:",random_word) #If player guessed the correct word
        break #exits the loop
