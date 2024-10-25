import random

# ● ┌ ┐ │ └ ┘ ─

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│         │",
        "│  ●   ●  │",
        "│         │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│    ●    │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}



while True:
    user = int(input("How many dice do you want to roll?: "))
    total = 0
    num_of_dice = []

    for num in range(user):
        num_of_dice.append(random.randint(1, 6))

    for num in num_of_dice:
        total += num

    for die in range(5):
        for line in num_of_dice:
            print(dice_art.get(line)[die],end="")
        print()

    print(f"Total = {total}")

    choice = input("Again? (Y/N): ").upper()
    if choice == "Y":
        pass
    else:
        break 
