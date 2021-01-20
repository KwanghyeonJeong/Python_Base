'''
quiz4)
Your school hosts a Python coding competition.
We decided to hold a comment event to increase attendance.
One will receive a chicken and three will receive a coffee coupon through a lottery among the commenters.
Create this program.

Rule 1: For convenience, assume that 20 people wrote the comments and the ID is 1 to 20.
Rule 2: Random draw regardless of comments, but not duplicated
Rule 3: Utilize "shuffle" and "sample" from "random" modules

<print example>
--Winner announcement--
chicken: 1
coffee:[2,3,4]
  -Congratulations !-

<Example of utilization>
form random import *
lst = [1,2,3,4,5]
print(lst)
# shuffle list
shuffle(lst)
print(lst)
# pick n In this case, n=1
print(sample(lst,1))
'''

# Anser)

















































































#################################################################
# Example)
'''
from random import *

# create things 1~20
users=range(1,21)

# save users to list
# check:print(users)
users=list(users)
# shuffle users
shuffle(users)
winners = sample(users,4)

print("--Winner announcement--")
print("chicken:{0}".format(winners[0]))
print("coffee:{0}".format(winners[1:]))
print("  -Congratulations !-")
'''