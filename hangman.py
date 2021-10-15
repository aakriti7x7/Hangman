
#Hangman


import random
from word import word
import string
from termcolor import colored
import inquirer

GAME_LEVEL = [
  inquirer.List('level',
                message="Please select game level",
                choices=['Easiest', 'Easy', 'Normal', 'Hard', 'Nightmare'],
            ),
]

GAME_LEVEL_MAPPING = {
  "Easiest" : 99,
  "Easy" : 10,
  "Normal" : 6,
  "Hard" : 3,
  "Nightmare" : 1,
}

def valid(word):
  w = random.choice(word)
  while '-' in word or ' ' in word:
    w= random.choice(word)

  return w.upper()


def hangman(game_level):

  w = valid(word)
  word_letter =  set(w)
  alphabet = set(string.ascii_uppercase)
  used_letter = set() # empty for now

  lives = game_level
  while len(word_letter)>0 and lives>0:

    print("\nyou have", lives,"lives left used: "," " .join(used_letter) )

    #list for[w o _ d]
    currentCondition=[letter if letter in used_letter else "_" for letter in w]
    print("current Condition: ", " ".join(currentCondition))

    user_letter = input('guess a letter: ').upper()

    if user_letter in alphabet - used_letter:
      used_letter.add(user_letter)
      
      if user_letter in  word_letter:
        word_letter.remove(user_letter)
      else:
        lives=lives - 1
    elif user_letter in used_letter:
      print(colored("already used, try smthing else", "red"))
      lives = lives - 1
    
    else:
      print(colored("invalid character", "red"))

  if lives==0:
    msg = colored("u died the word was ", "red")
    word_answer = colored(w, "magenta")
    print(f"{msg}: {word_answer}")
  else:
    msg = colored("yey u guessed ", "green")
    word_answer = colored(w, "magenta")
    print(f"{msg}: {word_answer}")


if __name__ == "__main__":
  # # print("type smthing to start\n")
  # user_input = input("type something to start then [ENTER]\n>> ")
  # print(colored(user_input, 'green'))

  answers = inquirer.prompt(GAME_LEVEL)
  game_level = GAME_LEVEL_MAPPING.get(answers["level"])

  hangman(game_level)
