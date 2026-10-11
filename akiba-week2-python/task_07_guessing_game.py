guessed = False
count = 0
secret_num = 7
while guessed == False and count <5:
    guess = int(input("Enter a guess: "))
    count += 1
    if guess == secret_num:
        guessed = True
        print(f"Congratulations!\nYou guessed the number in {count} attempts.")
    else:
        if count == 5:
            print("Game Over!")
        else:
            print("Try again")