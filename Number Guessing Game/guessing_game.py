import random

attempts = 0;
secret_number = random.randint(1,100);

while True:
    number = int(input("Guess the number between 1 and 100:"));
    attempts += 1;

    if number > secret_number:
        print("Too high!");
    elif number < secret_number:
        print("Too low!");
    else:
        print("Congratulations! You guessed the number in {} attempts.".format(attempts));
        break;
