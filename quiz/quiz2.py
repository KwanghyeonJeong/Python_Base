# quiz2)You recently created a new Coding Study Group. 
# # I study 4 times a month, but I decided to do 3 times online and 1 time offline.
# Create a program that sets an offline meeting date that meets the conditions below.

# Rule 1:Date must be randomly selected
# Rule 2:The monthly date is set within 28 days
# Rule 3:Excluded because study preparation is required on the 1st to 3rd of every month

# (print example)
# The offline study meeting date was selected as the x day of each month.

#use random module
from random import *
#Create a meeting date randomly between the 4th and 28th
d_day = randint(4,28) # 4~28
print("The offline study meeting date was selected as the",d_day,"day of each month.")


