import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "kiwi", "pear", "melon","mango","lemon","cherry","pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while "_" in display_word(word, guessed_letters) and incorrect_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter!")
            elif guess in word:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                incorrect_guesses += 1
                print("Incorrect guess. Try again.")
        else:
            print("Invalid input. Please guess a single letter.")

        print("Attempts left:", max_attempts - incorrect_guesses)
        print(display_word(word, guessed_letters))

    if "_" not in display_word(word, guessed_letters):
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you're out of attempts. The word was:", word)

hangman()
