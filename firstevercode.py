import random
import time
import sys

def print_slowly(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

test = "hi this is proof that im gonna be the next mark zuckerberg\n"
print_slowly(test)
print("ok,\nim gonna try to guess ur name okay?")
namedictionary = ["maria", "rob", "eric", "jared", "elle", "biff", "craig", "ruth", "ali", "aarij", "mark", "mel", "liam", "nathan", "leo", "what name ends with p", "what name ends with q", "esther", "jesus", "matt", "andrew", "keanu", "liv", "jax", "jay", "cruz"]
print("hmmmmmmmmmmmmmmmmm....")
lastletter = input("ok at least tell me the last letter? ")
filteredname = [word for word in namedictionary if word.endswith(lastletter)]
result_string = ', '.join(filteredname)
print(result_string + "??")
name = input("alright , just tell me ")
if lastletter.lower() != name[-1].lower():
    print("youd u lie about the last letter?? anyways")
elif name == result_string:
    print("NO WAY I GUESSED IT RIGHT")
else:
    name = name.strip().title()
    print(f"great!! Hi, {name}" + lastletter.lower() + lastletter.lower() + lastletter.lower())
age = input("how old r you? ")
agedifference = 16 - int(age)
if agedifference == 0:
    print("OMG WE ARE THE SAME AGE????")
if agedifference > 1:
    print("you are " + str(agedifference), "years younger than me!")
if agedifference < -1:
    print("you are " + str(abs(agedifference)), "years older than me!")
if agedifference == 1:
    print("you are " + str(agedifference), "year younger than me!")
if agedifference == -1:
    print("you are 1 year older than me!")
print("alright " + name, ", lets play a game.")
gameanswer = input("do you wanna play hangman? ")
if gameanswer == "no" or "nah" or "nope":
    print("well too bad, you can guess first")
elif gameanswer == "yes" or "yeah" or "sure" or "ok" or "yep":
    print("great decision!")
else:
    print("uhh ok, lets start!")

dictionary = ["halloween", 'cat', "methods", "exams", "dad", "jesus", "meow", "ice", "hunter", "blood", "painting",
              "invoice", "ambition", "brittle", "fei", "gary sucks"]
print("im thinking of a word...")
word = random.choice(dictionary)
numberofletters = len(word)
print("ok im done! the word has " + str(numberofletters), "letters!")

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def print_hangman(attempts):
    if attempts == 6:
        print("\n+---+")
        print("|")
        print("|")
        print("|")
        print("+----")
    elif attempts == 5:
        print("\n+---+")
        print("|   o")
        print("|")
        print("|")
        print("+----")
    elif attempts == 4:
        print("\n+---+")
        print("|   o")
        print("|   |")
        print("|")
        print("+----")
    elif attempts == 3:
        print("\n+---+")
        print("|   o")
        print("|  /|")
        print("|")
        print("+----")
    elif attempts == 2:
        print("\n+---+")
        print("|   o")
        print("|  /|\ ")
        print("|")
        print("+----")
    elif attempts == 1:
        print("\n+---+")
        print("|   o")
        print("|  /|\ ")
        print("|   /")
        print("+----")
    elif attempts == 0:
        print("\n+---+")
        print("|   o")
        print("|  /|\ ")
        print("|   /\ ")
        print("+----")

def hangman():
    word_to_guess = word
    guessed_letters = []
    attempts= 6


    while True:
        print("\nAttempts left", attempts)
        print_hangman(attempts)

        current_display = display_word(word_to_guess, guessed_letters)
        print("current word:", current_display)

        if current_display == word_to_guess:
            print(f"finally, {name}! u guessed the word", word_to_guess)
            break

        if attempts == 0:
            print("soz u lost the word was:", word_to_guess)
            break

        guess = input("guess a letter: "). lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("youve already guessed that!")
                guessed_letters.append(guess)
            elif guess in word_to_guess:
                print("slay")
                guessed_letters.append(guess)
            else:
                print("wrong. guess again")
                attempts -= 1
                guessed_letters.append(guess)
        else:
            print(f"just enter a single letter {name}" )

if __name__ == "__main__":
    hangman()





