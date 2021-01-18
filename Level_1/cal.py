'''
print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) #2^3=8
print(5%3) #나머지 구하기 2
print(10%3) #1
print(5//3) #몫 구하기 1
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
num += 2 #num에서 2 증가
print(num) #16
num *= 2 #num에서 2만큼 곱
print(num)
'''

'''
print(abs(-5)) # 절댓값 5
print(pow(4,2)) # 4^2 = 16
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5
'''

'''
#math 가져오기
from math import *

print(floor(4.99)) #내림. 4
print(ceil(3.14)) #올림. 4
print(sqrt(16)) #제곱근. 4
'''

'''
#랜덤함수
from random import *

# print(random()) #0.0~1.0미만 임의의 수
# print(random()*10) #0.0~10.0 미만 임의의 수

print(int(random()*10)) #0~10미만의 임의의 수
print(int(random()*10+1)) #1~10미만의 임의의 수

print(randrange(1,46)) #1~46미만 임의의 수 뽑기
print(randint(1,45)) # 1~45사이의 임의의 수 뽑기
'''
