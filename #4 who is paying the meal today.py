#4 who is paying the meal today

names_string = "Angela, Ben, Jenny, Michael, Chloe"

names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

count = len(names)
random_integer = random.randint(0,count -1)
pay = names[random_integer]
print(f"{pay} is going to buy the meal today!")