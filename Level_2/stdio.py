# basic
'''
print("Python","Java")
print("Python"+"Java")
print("Python","Java", sep=',')
print("Python","Java", sep=" vs ")
print("Python","Java","JavaScript", sep=" vs ")
'''

# Change the end of the sentence to '?' (default= \n)
'''
print("Python","Java", sep=',', end="?")
print("What's more interesting?")
'''

# sys
'''
import sys
print("Python","Java", file=sys.stdout)
print("Python","Java", file=sys.stderr)
'''

# exam score(dictionary)
'''
scores = {"Math":0, "Eng":50, "Code":100}
for subject, scores in scores.items():
    # print(subject,scores)
    print(subject.ljust(8),str(scores).rjust(4), sep=':')
'''

# 001, 002, 003
'''
for num in range(1,21):
    print("Wait number : "+str(num).zfill(3))
'''

# input : (Warning!) Save as str
'''
answer = input("Input Anything: ")
print(type(answer))
print("The value you entered is " + answer)
'''