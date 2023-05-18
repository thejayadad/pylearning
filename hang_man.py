
#setup word list
import random


word_list = ["school", "house", "cars"]
chosen_word = random.choice(word_list)

#selet random word asign to variable chosen_word
#guess letter and assign to guess make sure lower case
#make a list of "_" for each letter in the word
word_bank = []
print(chosen_word)
for guess_letter in chosen_word:
    word_bank += "_"
#check if letter guess is one of letters chosen
end_of_game = False

lives = 6


while not end_of_game:
    guess = input("Guess a letter ").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            word_bank[i] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"Current Lives {lives}")
        if lives == 0:
            end_of_game = True
            print("You loose")
            
    print(word_bank)

    if "_" not in word_bank:
        end_of_game = True
        print("You win!")

