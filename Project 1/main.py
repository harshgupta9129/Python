import random

def engine(computer_choice, user_choice):
    # Mapping numbers to names
    choices = {1: "Snake", 2: "Water", 3: "Gun"}
    print(f"\nComputer chose: {choices[computer_choice]}")
    print(f"You chose: {choices[user_choice]}")

    # Logic
    if computer_choice == user_choice:
        print("It's a Draw!")
    elif (computer_choice == 1 and user_choice == 2) or \
         (computer_choice == 2 and user_choice == 3) or \
         (computer_choice == 3 and user_choice == 1):
        print("Computer Wins! 💻")
    else:
        print("You Win! 🎉")

# Random choice for computer
a = random.choice([1, 2, 3])

print('''
Press 1 for Snake
Press 2 for Water
Press 3 for Gun
''')

# User input with validation
b = int(input("Enter Your Choice : "))
while b not in [1, 2, 3]:
    b = int(input("Enter a Valid Choice (1-3): "))

engine(a, b)
