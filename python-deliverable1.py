import math

your_name = input("Welocme to Mini Golf! What is your name? ")


num_holes = int(input("Would you like to play 3 or 6 holes of mini golf? Enter 3 or 6: "))


total_par = num_holes * 3


total_putts = 0


for hole in range(1, num_holes + 1):
    putts = int(input(f"Enter the number of putts for Hole {hole}: "))
    total_putts += putts


score_difference = total_putts - total_par


if score_difference > 0:
    print(f"Nice try, {your_name}... Your total score was: +{score_difference}.")
elif score_difference < 0:
    print(f"Great job, {your_name}! Your total score was: {score_difference}.")
else:
    print(f"Good game, {your_name}. Your total score was: 0.")





