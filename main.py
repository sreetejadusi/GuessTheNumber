#Import
import random

#Define Variables
class Variables:
        lower_limit = 0
        upper_limit = 100
        tries = 0


#Game Begins
class Start:
    print(f"I will think of a number between {Variables.lower_limit} and {Variables.upper_limit}, and you will have to guess it.")

    def __init__(self):
        number = random.randint(Variables.lower_limit, Variables.upper_limit)
        tries = Variables.tries

        try:
            while True:
                guess = int(input("Give a Guess: "))

                if guess == number:
                    print(f"Great! you did it in {tries + 1} tries.")
                    break

                elif guess < number:
                    print("The number you guessed is low.")

                elif guess > number:
                    print("The number you guessed is high.")

                tries = tries + 1

        except ValueError:
            print("You can only input numbers")

        finally:
            print("Let's Restart!")
            start = Start()

#To Initialize Game
start = Start()


#A Code By Sree Teja Dusi
#GitHub: https://github.com/sreetejadusi
#LinkedIn: https://linkedin.com/in/sreetejadusi
#Website: https://sreetejadusi.me
#Twitter: https://twitter.com/sreetejadusi
#Instagram: https://instagram.com/sreeteja_dusi
#Facebook: https://facebook.com/sreetejadusi
