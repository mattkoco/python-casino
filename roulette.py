import random

# all of the roulette wheel possible spin number thingies
numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8,
           23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

# your betting options
outcomes = ["red", "black", "green"]

# if i need to explain this then you havent seen a computer screen in your life.
print("Welcome to the roulette game!")

# bet your life away
bet = input("Enter your bet (red, black, or a number): ")

# spinarooni
result = random.choice(numbers)

# this determines the outcome
if result in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
    outcome = "red"
elif result in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
    outcome = "black"
else:
    outcome = "green"

# checks if you make money (bad) or lose money (good)
if bet.lower() == outcome:
    print(f"The roulette landed on {result} {outcome}, you win!")
else:
    print(f"The roulette landed on {result} {outcome}, you lose.")

# !OBVIOUSLY NOT REAL GAMBLING NO REAL MONEY INVOLVEMENT!
