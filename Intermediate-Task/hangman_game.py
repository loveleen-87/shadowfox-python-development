import random

# word list
words = ["python", "machine", "apple", "developer", "car", "knife", "internship"]

# hangman stages (same as yours)
stages = [
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
""",
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
""",
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========
""",
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========
""",
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========
""",
    """
   -----
   |   |
   O   |
       |
       |
       |
=========
""",
    """
   -----
   |   |
       |
       |
       |
       |
=========
"""
]

# select word
word = random.choice(words)
guessed_letters = []   # store correctly guessed letters
lives = 6

print("\n🎮 Welcome to Hangman Game!")
print(f"Hint: The word has {len(word)} letters.\n")

# game loop
while lives > 0:
    # build the current display (e.g., "_ _ a _ _")
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word:", display)

    # win check – all letters have been guessed
    if all(letter in guessed_letters for letter in word):
        print(f"\n🎉 Congratulations! You guessed the word: {word}")
        break

    # get a new guess
    guess = input("Guess a letter: ").lower()

    # input validation
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Enter only ONE alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed this letter.\n")
        continue

    guessed_letters.append(guess)

    # check if the guess is correct
    if guess not in word:
        lives -= 1
        print(f"\n💔 Wrong guess! You have {lives} lives left.")
        print(stages[lives])   # stages[6] = empty, stages[0] = full hangman
    else:
        print("✅ Correct guess!\n")

# if the loop ended because lives reached 0
if lives == 0:
    print(f"\n💀 Game Over! The word was: {word}")
