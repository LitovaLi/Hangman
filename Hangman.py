#import random
def cls(): print("\n" * 100)
tries1 = """|
|
|
|
|
|"""
tries2 = """|----
|
|
|
|
|"""

tries3 = """|----
|   |
|
|
|
|"""

tries3 = """|----
|   |
|   o
|   
|
|"""

tries4 = """|----
|   |
|   o
|   |
|
|"""

tries5 = """|----
|   |
|   o
|  /|
|
|"""

tries6 = """|----
|   |
|   o
|  /|\\
|
|"""

tries7 = """|----
|   |
|   o
|  /|\\
|  / 
|"""

tries8 = """|----
|   |
|   o
|  /|\\
|  / \\
|"""
human = [tries1, tries2, tries3, tries4, tries5, tries6, tries7, tries8]
print("H A N G M A N")
menu = int(input('Type 1 to play the game, 2 to quit: '))
print()
while menu == 1:
    #variants = ["индульгенция", "облигация", "эмиграция", "мотивация"]
    #word = random.choice(variants)
    word = input("Write a word: ")
    cls()
    hint = list(len(word) * "-")
    tries = 8
    n = 0
    set_letters = set()

    while tries > 0:
        print(''.join(hint))
        letter = input("Input a letter: ")

        if letter in set_letters:
            print("You already typed this letter")

        elif letter == word:
            hint = word
            print('You guessed the word!')
            print('You survived!')
            print()
            break

        elif len(letter) > 1:
            print("You should input a single letter")

        elif letter.isascii() and letter.islower():
            if letter not in set(word):
                tries -= 1
                print("No such letter in the word")
                print(human[n])
                n += 1
                print("Attempts: ", tries)
            else:
                for j in range(len(word)):
                    if word[j] == letter:
                        hint[j] = letter
        else:
            print("It is not an ASCII lowercase letter")

        if len(letter) == 1:
            set_letters.add(letter)

        if "-" in hint and tries == 0:
            print("You are hanged!")
            print("Word - ", word)
            print()
            break
        elif "-" not in hint:
            print("You guessed the word", word)
            print("You survived!")
            print()
            break
        print()
    menu = int(input('Type 1 to play the game, 2 to quit: '))
    print()
