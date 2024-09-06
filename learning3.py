def new_game():
    guesses = []


    for key in questions:
        print("--------------------------------------------")
        print(key)
        for i in Options:
            print(i)
            guesses = input("Your answer?: ")


















questions = {"Who is the first president of Indonesia?": "A",
             "What is 1+1?": "B",
             "Where is monas located?": "B",
             "When is Indonesia independence day?": "D"
             }

Options = [["A. Soekarno", "B. Soeharto", "C. Jokowi", "D. Megawati"],
           ["A. 21, B. 2", "C. 5", "D. 19"],
           ["A. Singkawang", "B. Jakarta", "C. Depok", "D. Bandung"]]

new_game()