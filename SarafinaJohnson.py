import random

def show_characters(count):
    # Characters pool: Pocoyo, Elly, and Pato
    characters = [
        ("Pocoyo", "👦🏼"),
        ("Elly", "🐘"),
        ("Pato", "🦆")
    ]

    # Pick one randomly
    character_name, character_icon = random.choice(characters)

    print(f"How many {character_name}s do you see?")
    for i in range(count):
        print(character_icon, end=" ")
    print("\n")

    return character_name  # So we can refer back later


def get_valid_number():
    user_input = input("Type how many you see: ")
    while not user_input.isdigit():
        print("Oops! That’s not a number. Try again!")
        user_input = input("Type how many you see: ")
    return int(user_input)


def play_character_counting_game():
    print("Hey there! Let’s count Pocoyo and his friends together!\n")

    playing = True
    while playing:
        count = 1
        while count <= 10:
            character_name = show_characters(count)
            guess = get_valid_number()

            if guess == count:
                print(f"Yay! You counted the {character_name}s correctly!\n")
                count += 1
            else:
                print("Hmm... Not quite. Let’s try again!\n")

        print("You did it! You counted all the characters! High five!\n")

        # Ask if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            playing = False
            print("Okay! See you next time, little superstar!")

# Start the game
play_character_counting_game()