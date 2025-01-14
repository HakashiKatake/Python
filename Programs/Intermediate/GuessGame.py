target = random.randint(1, 10)
guess = None
while guess != target:
    guess = int(input("Guess the number (1-10): "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("You got it!")