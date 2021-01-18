# while

# case 1
customer = "Tom"
index = 5
while index >= 1:
    print("{0}, Ready your coffee".format(customer))
    index-=1
    if index == 0:
        print("The coffee has been disposed of")

# case 2 Infinite Loop
# if you want to exit loop, input (ctrl + c) in terminal
customer = "Steve"
index = 1
while True:
    index += 1
    print("{0}, Ready your coffee {1}".format(customer,index))

