#!/usr/bin/env python3
#Step 2
import logo
import random
import stages
import word_list
stages = stages.stages
logo = logo.logo
word_list =word_list.word_list


chosen_word = random.choice(word_list)

print(logo)
lives= 6
chosen_word_length=len(chosen_word)
print(f"The number of words are {chosen_word_length}")
      
display =[]
for x in chosen_word:
     display += "_"


end_of_game = False
while not end_of_game:
    user_input= input("Now choose the letter you think or someone DIES!: ")

    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if letter == user_input:
            display[position]= letter
    print("".join(display))
    
    if "_" not in display:
        end_of_game=True
        final=(f"You win, the word was: {chosen_word}")
        print(final)
    if user_input not in chosen_word:
        print(f"Psst.. This word is not present! Haha only {lives -1}  lives remaining!")
    if user_input not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game=True
            print(f"You Loose. THE WORD WAS {chosen_word}")
    print(stages[lives])
