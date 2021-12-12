import random
from art import logo,stages
from words import word_list
print(logo)
word = random.choice(word_list)
print(word)
guess = []
past_guesses=""
lives = 6
for letter in word:
    guess.append("_")
print(guess)
while(lives>0):
    print(stages[lives])
    if("_" in guess):
        letter = input("guess a letter: ").lower()
        if(letter not in past_guesses):
            past_guesses += letter
            if (letter in word):
                for index in range(len(word)):
                    if(word[index]==letter):
                        guess[index]=letter
                print(guess)   
            else:
                lives-=1
                
                if(lives==0):
                    print(stages[0])
                    print(f"you lose, the word was {word}")
                else:
                    print(f"the word does not contain {letter}, please try again")
        else:
            print("you already guessed that letter!")
    else:
        print(f"you win, the word was {word}")
        break
