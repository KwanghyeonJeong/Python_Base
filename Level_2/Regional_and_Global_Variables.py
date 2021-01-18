gun = 10

def checkpoint(soldiers):
    # gun init
    gun=20
    gun = gun - soldiers
    print("[in function]: {0}".format(gun))

def All_check(soldiers):
    # init global variables
    global gun
    gun = gun - soldiers
    print("[in function(global variables)]: {0}".format(gun))

def checkpoint_ret (gun,soldiers):
    gun = gun - soldiers
    #return
    return gun

print("guns: {0}".format(gun))

checkpoint(2)
All_check(4)
print("guns: {0}".format(gun))

gun = checkpoint_ret(gun,2)
print("guns: {0}".format(gun))


