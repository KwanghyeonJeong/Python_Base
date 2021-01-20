#print("a" + "b") ->ab
#print("a" , "b") ->a b

#method 1
'''
print("I'm %d years old" % 26)
print("I like %s" % "bananas")
print("String Apple's first alphabet is %c" %'A')
'''

# %s
'''
print("I'm %s years old" % 26)
print("What i really like color are %s and %s" % ("Blue","Red"))
'''

#method 2
'''
print("I'm {} years old" .format(26))
print("I like {} and {}" .format("Blue","Red"))
print("I like {0} and {1}" .format("Blue","Red"))
print("I like {1} and {0}" .format("Blue","Red"))
'''

#method 3
'''
print("I'm {age} years old, I like {color}".format(age=26,color="Blue"))
print("I'm {age} years old, I like {color}".format(color="Blue",age=26,))
'''

#method 4 (Version 3.6 or later)
'''
age =26 #var
color = "Red"
# 'f' must be first 
print(f"I'm {age} years old, I like {color}")
'''
