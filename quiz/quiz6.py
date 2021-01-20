'''
quiz6)
Write a program to get standard weight.

Rule 1: Standard weight is calculated within a suitable function
        * Function name: std_weight
        * Forwarding value: height(m), gender

Rule 2: Standard weight displayed to second decimal place

(example)
A 175cm tall man's standard weigh is 67.38kg.
'''
# Anser)

















































































#################################################################
# Example)
'''
#gendar: "man" or "woman"
def std_weight(height,gender):
    if (gender == "man"):
        return height * height * 22
    else:
        return height * height * 21

# "man" or "woman"
gender = input("What is your gender?")
# cm
height = int(input("how tall are you?"))
# Display up to second decimal place
weight = round(std_weight(height/100,gender),2)

print("A {0}cm tall man's standard weight is {1}kg.".format(height,weight))
'''
