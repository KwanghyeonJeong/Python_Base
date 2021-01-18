python = "python is Amazing"
print(python.lower()) #lowercase
print(python.upper()) #capitalcase
print(python[0].isupper()) #is first letter capitalcase?
print(len(python)) # HOW long (str)python?
print(python.replace("python","Java")) #replace "Python" -> "Java"

index=python.index('n') # where is 'n'? 
print(index) #5 "Pytho'n' is Amazing"
index=python.index('n', index + 1) # , index + 1 = start point
print(index) #15 "Python is Amazi'n'g"

print(python.find("Java")) # -1 there(str Python) is no "Java" 
#print(python.index("Java")) #error : It doesn't work even after  this.

print(python.count('n')) # how many do it have 'n'?