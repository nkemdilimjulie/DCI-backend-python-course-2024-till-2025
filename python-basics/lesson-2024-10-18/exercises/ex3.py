import random

guess = ""
toss_sides = ("heads", "tails")
number_of_trails = 5

while (
    guess := input("Guess the coin toss! Enter heads or tails: ")
    != toss_sides[random.randint(0, 1)]
):
    if not number_of_trails:
        print("Nope. You are really bad at this game.")
        break

    print("Nope! Guess again!")
    number_of_trails -= 1
else:
    print("You got it!")


# guess = ""
# while guess not in ("heads", "tails"):
#     print("Guess the coin toss! Enter heads or tails:")
#     guess = input()
# toss = random.randint(0, 1)  # 0 is tails, 1 is heads
# if toss == guess:
#     print("You got it!")
# else:
#     print("Nope! Guess again!")
#     guesss = input()
#     if toss == guess:
#         print("You got it!")
#     else:
#         print("Nope. You are really bad at this game.")
