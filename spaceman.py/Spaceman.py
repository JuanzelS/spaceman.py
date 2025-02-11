import random

def hangman_game():
    print("Welcome to Hangman")
    print("-------------------------------------------")
    secret_word = get_secret_word()
    is_word_guessed(secret_word, [])

'''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
'''
def get_secret_word():
    with open('words.txt', 'r') as f:
        words_list = f.readlines()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list).strip()
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    # Initialize variables
    word_length = len(secret_word)
    guessed_word = ["_"] * word_length
    attempts_left = 7
    guessed_letters = []

    while attempts_left > 0 and "".join(guessed_word) != secret_word:
        # Display the current state of the game
        display_hangman(secret_word, guessed_word, attempts_left)

        # Display guessed letters
        print("Guessed letters:", " ".join(guessed_letters))

        # Prompt the user for a guess
        guess = input("Guess a letter: ").lower()

        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the guessed letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed '{}'.".format(guess))
            continue

        # Check if the guessed letter is in the word
        if guess in secret_word:
            for i in range(word_length):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
            print("Correct guess: '{}' is in the word.".format(guess))
        else:
            # Decrement the attempts left
            attempts_left -= 1
            # Add the guessed letter to the list
            guessed_letters.append(guess)
            print("Incorrect guess: '{}' is not in the word.".format(guess))

    if "".join(guessed_word) == secret_word:
        display_hangman(secret_word, guessed_word, attempts_left)
        print("Congratulations! You guessed the word:", secret_word)
    else:
        display_hangman(secret_word, guessed_word, attempts_left)
        print("Out of attempts. The word was:", secret_word)

def display_hangman(word, guessed, attempts_left):
    print("Word:", " ".join(guessed))
    print("Attempts left:", attempts_left)

if __name__ == "__main__":
    hangman_game()
