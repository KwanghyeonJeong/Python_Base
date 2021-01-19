'''
quiz7)
There is a delicious chicken restaurant in the neighborhood 
where there are always waiting customers.

We'd like to make an automatic ordering system 
to reduce the number of chicken dishes for waiting guests.

Create a system with appropriate exception syntax.

Rule 1: If it is less than or non-numeric than 1, 
        treat it is treated as ValueError.

Rule 2: The total amount of chicken 
        that waiting customers can order is limited to 20.

Rule 3: Generate a custom error [SoldOutError] 
        when chicken is exhausted and exit the program.
'''
# custom error
class SoldOutError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

# var init
chicken = 20
waiting = 1
# loop
while True:
    try:
        print("Orderable Chicken: {0}s".format(chicken))
        order = int(input("How many chickens would you like to order?"))
        if order <= 0:
            raise ValueError
        if order >= 1:
            if chicken - order > 0:  
                print("[waiting[{0}]]: {1} chicken has been ordered."\
                    .format(waiting,order))
                chicken -= order
                waiting += 1
            elif chicken - order == 0:
                
                print("[waiting[{0}]]: {1} chicken has been ordered."\
                    .format(waiting,order))
                chicken -= order
                waiting += 1
                raise SoldOutError("We don't have chicken in stock.")
            elif chicken - order < 0:
                raise ValueError
        else:
            raise ValueError

    except ValueError:
        print("The value is not valid.")

    except SoldOutError as err:
        print(err)
        break