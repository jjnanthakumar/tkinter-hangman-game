import random
import requests
import json


def randomword(name, serviceurl='https://api.datamuse.com/words?'):
    char = random.choice(list(name))
    serviceurl += 'sp=' + char + '*' + '&max=500'

    # get api key from here: https://developer.wordnik.com/#wordnikUsername  ( it takes 1 week to get your api key) - be patient
    r = requests.get(serviceurl)
    # print(serviceurl)
    # print(r.content)
    try:
        data = r.content
        data = json.loads(data)
    except:
        raise ValueError("Datamuse Server Problem! Hang on For a minute :)")
    return random.choice([ele['word'] for ele in data if len(ele['word']) > 5])

def hangmangame():
    name = input("Enter Your Name: ")
    print(f"Hello {name.capitalize()}, Welcome to Hangman Game!!")
    print(
        "Start Guessing....\nRules:\n1) Please Don't type Repeated characters\n2) Only one Character is Allowed for guessing\n3) Numbers Not Allowed\n")
    hidden_word = randomword(name).replace(' ', '')

    turns = 0
    hashed = list("_" * len(hidden_word))
    print(' '.join(hashed))
    while (turns < 10):
        # if turns == 0:
        #     print(' '.join(hashed))
        find = input("Guess a Character: ")
        if len(find) != 1 or not find.isalpha():
            raise ValueError("Value must be single character!!")
        if find not in hidden_word:
            turns += 1
        for i, j in enumerate(hidden_word):
            if j == find:
                hashed[i] = j
        print(' '.join(hashed))
        print(f"Remaining Turns : {10 - turns}")

        if '_' not in hashed:
            print(f"Congragulations {name}! You won")
            break
    else:
        print("You Lose :(")
        print(f"Answer is : {hidden_word}")
    check = input("Do you want to Play Again Y/N : ")
    if check.lower() == 'y' or check.lower() == 'yes':
        hangmangame()
    print(f"Thanks For Playing {name} :)")


hangmangame()
