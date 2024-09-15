import sys
import random
def main():
    number = random.randint(1, 100)
    print("Between 1 and 100.")

    def guess_num(num):
        if num > number + 15:
            print("your guess is too high.")
        elif num < number - 15:
            print("your guess is too low.")
        elif num != number:
            print("You're close.")
        else:
            print("Congrats your guess is correct!\U0001F44F\U0001F3FB\U0001F44F\U0001F3FB\U0001F44F\U0001F3FB")
            sys.exit()
        
    limit = 10
    while limit > 0:
        user_input = int(input("Guess the number: "))
        guess_num(user_input)
        limit -= 1
    print("Game Over!")

if (__name__) == "__main__":
    main()