import random

def hangman():
    words = ['python', 'hangman', 'game', 'player', 'guess', 'word']
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word contains", len(secret_word), "letters.")


    while True:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word)
        print("Attempts left:", attempts)

        if "_" not in display_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Wrong guess!")

            if attempts == 0:
                print("Game over! You ran out of attempts.")
                print("The word was:", secret_word)
                break

hangman()









