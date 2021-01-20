# quiz3) Creating a program that creates passwords by site
# Rule 1: Excluding http:// parts, -> google.com
# Rule 2: Excluding parts since the first meeting (.) -> google
# Rule 3: 
#     the first three digits of the remaining characters(goo) 
# +   The number of characters(6)
# +   The number of 'e's in the letter(1)
# +   '!'

# Anser)

















































































#################################################################
# Example.1)
'''
#url
url="http://google.com"

#Rule 1
    # check: print(Password)
    #Password:google.com
Password=url[7:]

#Rule 2
    # check: print(Password.index('.'))
    # check: print(Password)
    # Password:google
Password=Password[:Password.index('.')]
# The number of characters
Password_Num=len(Password)
# The number of 'e's in the letter
Password_Num2=Password.count('e')

#Rule 3
#     the first three digits of the remaining characters(goo) 
# +   The number of characters(6)
# +   The number of 'e's in the letter(1)
Password=Password[:3]

Password=Password+str(Password_Num)+str(Password_Num2)+'!'

# print Password
print(Password)
'''

# Example.2)
'''
url = "http://google.com"
# Rule 1
my_str = url.replace("http://", "")
#print(my_str)

# Rule 2
my_str=my_str[:my_str.index('.')]

# Rule 3
Password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print("{0} 의 비밀번호는 {1}입니다.".format(url,Password))

'''



