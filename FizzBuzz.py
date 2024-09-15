class FizzBuzz:
    def __init__(self):
        self.number = int(input("Enter a number: "))
        

    def play(self):
        for _  in range(self.number + 1):
            if _ == 0:
                continue
            elif _ % 3 == 0 and _ % 5 == 0:
                print("FizzBuzz")
            elif _ % 3 == 0:
                print("Fizz")
            elif _ % 5 == 0:
                print("Buzz")
            else:
                print(_, )

if (__name__) == "__main__":
    game = FizzBuzz()
    game.play()