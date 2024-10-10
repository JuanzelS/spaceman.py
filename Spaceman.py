import random

def hangman_game():
    print("Welcome to Hangman")
    print("-------------------------------------------")

     f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

    # Initialize variables
    word_length = len(randomWord)
    guessed_word = ["_"] * word_length
    attempts_left = 7
    guessed_letters = []

    while attempts_left > 0 and "".join(guessed_word) != randomWord:
        # Display the current state of the game
        display_hangman(randomWord, guessed_word, attempts_left)

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
        if guess in randomWord:
            for i in range(word_length):
                if randomWord[i] == guess:
                    guessed_word[i] = guess
            print("Correct guess: '{}' is in the word.".format(guess))
        else:
            # Decrement the attempts left
            attempts_left -= 1
            # Add the guessed letter to the list
            guessed_letters.append(guess)
            print("Incorrect guess: '{}' is not in the word.".format(guess))

    if "".join(guessed_word) == randomWord:
        display_hangman(randomWord, guessed_word, attempts_left)
        print("Congratulations! You guessed the word:", randomWord)
    else:
        display_hangman(randomWord, guessed_word, attempts_left)
        print("Out of attempts. The word was:", randomWord)

def display_hangman(word, guessed, attempts_left):
    print("Word:", " ".join(guessed))
    print("Attempts left:", attempts_left)

if __name__ == "__main__":
    hangman_game()
