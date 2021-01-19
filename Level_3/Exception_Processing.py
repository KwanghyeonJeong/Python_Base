
try:
    print("Divide Only Calculator")
    nums=[]
    nums.append(int(input("first number = ")))
    nums.append(int(input("second number = ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0}/{1}={2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("Error !")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("Error ! I don't know..")
    print(err)