import random

word_list = ["apple", "banana", "cherry", "grape", "orange", "strawberry"]


def choose_word():
    return random.choice(word_list)


def play_game():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = len(word_to_guess) + 2  
    print("Welcome to the Word Guessing Game!")
    print("You have {} attempts to guess the word.".format(attempts))

    while attempts > 0:
        word_display = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                word_display += letter
            else:
                word_display += "_"

        print("Word to guess: " + word_display)
        print("Guessed letters: " + ", ".join(guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
                if word_display == word_to_guess:
                    print("Congratulations! You guessed the word: " + word_to_guess)
                    break
            else:
                print("Oops! That letter is not in the word.")
                guessed_letters.append(guess)
                attempts -= 1
        else:
            print("Please enter a single letter.")

    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was: " + word_to_guess)

if __name__ == "__main__":
    play_game()
