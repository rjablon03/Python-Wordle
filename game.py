import random

def compare_to_answer(characters, user):
    count = 0
    for i in user:
        if i in characters and i != characters[count]:
            print(i + " !")
            count+=1
        elif i == characters[count]:
            print(i)
            count+=1
        else:
            print(i + ' !!!')
            count += 1

words = ['maple', 'honey', 'hills', 'there', 'apple', 'snake', 'pools', 'tweet', 'sweet', 'adult', 'anger', 'smile', 'beach', 'ocean', 'shark', 'shake',
         'meals', 'fling', 'gleam', 'solar', 'slain', 'space', 'brain', 'shame', 'crane', 'eagle', 'taxes', 'crime', 'rails']
answer = words[random.randint(0, len(words) - 1)]
char_list = []
for i in answer:
    char_list.append(i)

correct_guess = False
num_guesses = 0

print()
print("I am thinking of a 5 letter word and I want you to guess it! Please make sure that your guesses are all lowercase!!!")
print("'!' means the letter is in the word but in the wrong position, and '!!!' means the letter is not in the word.")
print("If there is no symbol, the letter is in the right spot! You have 5 guesses, good luck!\n")
while correct_guess == False:
    if num_guesses == 5:
        print("\nYou lose. The answer was '" + answer + "'")
        break
    user_guess = input()
    while len(user_guess) != 5:
        user_guess = input()
    if user_guess == answer:
        print('You win!')
        correct_guess = True
    else:
        compare_to_answer(char_list, user_guess)
        print()
        num_guesses += 1