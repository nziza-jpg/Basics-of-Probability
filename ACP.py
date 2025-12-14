import random

# Probability of getting a 6
probability = 1 / 6
print("Probability of getting a 6:", probability)

# Roll the dice
dice = random.randint(1, 6)
print("Dice rolled:", dice)

# Check condition
if dice == 6:
    print("Game can be started")
else:
    print("Roll again. Best of luck!")