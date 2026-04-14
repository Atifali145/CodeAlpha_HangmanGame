import random

# Predefined word list (5 words)
words = ["apple", "tiger", "chair", "robot", "plant"]

# Select a random word
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Create display version of word
display_word = ["_"] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.\n")

while incorrect_guesses < max_attempts and "_" in display_word:
    print("Word:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!\n")
        # Reveal letters in word
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong! Attempts left: {max_attempts - incorrect_guesses}\n")

# Final result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)