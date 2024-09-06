import random
def guess(x):
    random_number = random.randint(1, x)
    guess = None
    while True:
        try:
         guess = int(input("Guess the number from 1-10: "))
        except:
         print("Please enter a number!")
         continue

        if guess < random_number:
            print("Sorry wrong number! It's higher.Try again!")
        elif guess > random_number:
            print("Sorry wrong number! It's lower.Try again!")
        elif guess == random_number:
            print(f"Your guess is right! It's {random_number}")
            play_again()
def play_again():
    Player = input("Play again (Yes/No): ")
    Player = Player.upper()
    if Player == "YES":
        return True
    else:
        return False


guess(10)

