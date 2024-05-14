import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

def draw_hangman(incorrect_guesses):
    stages = [
        """
            _______
           |      |
           |
           |
           |
           |
          _|_
        """,
        """
            _______
           |      |
           |      O
           |
           |
           |
          _|_
        """,
        """
            _______
           |      |
           |      O
           |      |
           |
           |
          _|_
        """,
        """
            _______
           |      |
           |      O
           |     /|
           |
           |
          _|_
        """,
        """
            _______
           |      |
           |      O
           |     /|\\
           |
           |
          _|_
        """,
        """
            _______
           |      |
           |      O
           |     /|\\
           |     /
           |
          _|_
        """,
        """
            _______
           |      |
           |      O
           |     /|\\
           |     / \\
           |
          _|_
        """
    ]
    return stages[incorrect_guesses] if incorrect_guesses < len(stages) else stages[-1]  # Use the last stage if incorrect_guesses exceeds available stages

def hangman():
    secret_word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = len(secret_word) + 1  # Maximum incorrect guesses allowed before game over

    print("Welcome to Hangman!")
    print("Try to guess the secret word.")

    while incorrect_guesses < max_attempts - 1:
        print("Word:", display_word(secret_word, guessed_letters))
        print("Incorrect guesses left:", max_attempts - 1 - incorrect_guesses)
        print(draw_hangman(incorrect_guesses))
        
        guess = input("Enter a letter or the full word guess: ").lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in secret_word:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                incorrect_guesses += 1
                print("Incorrect guess.")
        elif len(guess) == len(secret_word) and guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' correctly!")
            return  # Exit the function after congratulating the player
        else:
            print("Incorrect guess.")

    if incorrect_guesses == max_attempts - 1:
        print(f"Sorry, you've used all your attempts. The secret word was '{secret_word}'.")

if __name__ == "__main__":
    hangman()
