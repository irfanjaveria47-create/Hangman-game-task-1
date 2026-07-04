import random

# List of words
words = ["python", "computer", "programming", "developer", "keyboard", "internet"]

#/ Choose a random word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while attempts > 0:
    display_word = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", attempts)

# Game over
if attempts == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", word)