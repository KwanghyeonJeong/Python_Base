'''
print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) #2^3=8
print(5%3) #remainder 2
print(10%3) #1
print(5//3) #quotient 1
print(10//3) #3

print(10>3) #True
print(4>=7) #False
print(10<3) #False
print(5<=5) #True

print(3==3) #True
print(4==2) #False
print(3+4==7) #True
print(1!=3) #True
print(not(1!=3)) #False
'''

'''
print((3>0) and (3<5)) #True
print((3>0) & (3<5)) #True

print((3>0) or (3>5)) #True
print((3>0) | (3>5)) #True
'''

'''
print(5>4>3) #True
print(5>4>7) #Flase
'''

'''
print(2+3*4) #14
print((2+3)*4) #20

num=2+3*4 
print(num) #14
num += 2 #num increase by 2
print(num) #16
num *= 2 #num multiple by 2
print(num)
'''

'''
print(abs(-5)) # Absolute value 5
print(pow(4,2)) # 4^2 = 16
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5
'''


#math import
'''
from math import *

print(floor(4.99)) #down. 4
print(ceil(3.14)) #up. 4
print(sqrt(16)) #Square root. 4
'''


#random import
'''
from random import *

print(random()) #0.0 ~ Less than 1.0
print(random()*10) #0.0 ~ Less than 10.0 

print(int(random()*10)) #0 ~ Less than 10
print(int(random()*10+1)) #1 ~ Less than 10

print(randrange(1,46)) #1 ~ Less than 46
print(randint(1,45)) # 1 ~ Less than 45
'''
