# for

# print("wait_num:1")
# print("wait_num:2")
# print("wait_num:3")
# print("wait_num:4")

# case 1
for waiting_num in [0,1,2,3,4]:
    print("wait_num:{0}".format(waiting_num))

# case 2
for waiting_num in range(1,6): # 1~5
    print("wait_num:{0}".format(waiting_num))

# case 3
starbucks = ['A','B','C']
for customer in starbucks:
    print("{0}, Take your coffee".format(customer))