# dictionary

# 3 - steve 10 - sarah
cabinet = {3:"steve",100:"sarah"} 
print(cabinet[3])
print(cabinet.get(3))
print(cabinet[100])

# key error
# print(cabinet[5])

# no error
print(cabinet.get(5))
# none + message
print(cabinet.get(5,"empty"))

print(3 in cabinet) # True
print(5 in cabinet) # False

# new thing
print(cabinet)
cabinet[3]="Tom"
print(cabinet)

# del thing
del cabinet[3]
print(cabinet)

# print keys only
print(cabinet.keys())

# print values only
print(cabinet.values())

# print keys and values
print(cabinet.items())

# clear dictionary
cabinet.clear
print(cabinet)
