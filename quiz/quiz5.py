'''
quiz5)
You are a taxi driver who uses public transportation services.

When you have a chance to match 50 passengers, write a program to get the total number of passengers on board.

Rule 1: The travel time per passenger is determined by random numbers between 5 and 50 minutes.
Rule 2: You should only match passengers between 5 and 15 minutes of time.

'''
# Anser)

















































































#################################################################
# Example)
'''
from random import *
cnt = 0
mark = 'O'
# i : 1~50
for i in range(1,51):
    # time = 1~50
    time = randrange(1,51)
    if 5 <= time <= 15:
        mark = 'O'
        print("[{0}] {1}passengers (required: {2}min)".format(mark,i,time))
        cnt += 1
    else:
        mark = ' '
        print("[{0}] {1}passengers (required: {2}min)".format(mark,i,time))
print("The number of passengers is {0}.".format(cnt))
'''