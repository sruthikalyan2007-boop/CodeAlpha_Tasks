import random

# Predefined categories and words
CATEGORIES = {
    "programming": ["python", "developer", "computer", "keyboard", "variable"],
    "animals": ["elephant", "giraffe", "penguin", "kangaroo", "dolphin"],
    "countries": ["australia", "brazil", "canada", "denmark", "egypt"],
    "movies": ["inception", "avatar", "titanic", "gladiator", "matrix"]
}

def play_hangman_round(target_word):
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    
    while incorrect_guesses < max_incorrect_guesses:
        # Display the word with blanks (-) for unguessed letters
        display_word = ""
        for letter in target_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "-"
                
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        # Check for win condition
        if "-" not in display_word:
            print(f"\nCongratulations! You guessed the word '{target_word}' correctly!")
            return True # Won the round
            
        # Basic console input
        guess = input("Enter a letter: ").lower()
        
        # Handle invalid inputs
        if len(guess) != 1:
            print("Invalid input! Please enter exactly one letter at a time.")
        elif not guess.isalpha():
            print("Invalid input! Please enter only alphabetic characters.")
        elif guess in guessed_letters:
            print("You already guessed that letter! Try a different one.")
        else:
            # Valid guess
            guessed_letters.append(guess)
            
            if guess not in target_word:
                print(f"Sorry, '{guess}' is not in the word.")
                incorrect_guesses += 1
    # Check for loss condition
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame Over! You've run out of guesses.")
        print(f"The word was '{target_word}'.")
        return False # Lost the round

def get_category():
    print("\nAvailable categories:")
    for cat in CATEGORIES.keys():
        print(f"- {cat.title()}")
    
    while True:
        choice = input("Enter a category from the list above: ").lower()
        if choice in CATEGORIES:
            return choice
        print("Invalid category. Please try again.")

def get_num_rounds():
    while True:
        try:
            rounds = int(input("\nHow many rounds would you like to play? "))
            if rounds > 0:
                return rounds
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def play_game():
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    
    num_rounds = get_num_rounds()
    category = get_category()
    
    words_list = CATEGORIES[category].copy()
    
    total_score = 0
    
    for round_num in range(1, num_rounds + 1):
        print(f"\n--- Round {round_num} of {num_rounds} ---")
        
        # Make sure we don't run out of words
        if not words_list:
             print("You've played all words in this category! Resetting the word list.")
             words_list = CATEGORIES[category].copy()
             
        target_word = random.choice(words_list)
        words_list.remove(target_word) # don't repeat words if possible
        
        won = play_hangman_round(target_word)
        
        if won:
            total_score += 10
            print("You earned 10 points!")
        else:
            total_score -= 5
            print("You lost 5 points.")
            
        print(f"Current Score: {total_score}")
        
    print(f"\n--- Game over! ---")
    print(f"Your final score after {num_rounds} rounds is: {total_score}")

if __name__ == "__main__":
    play_game()
