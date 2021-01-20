# module

'''
The module must be in the same path as the file on which 
the module is intended.

Modules are available in folders 
where Python libraries are clustered.
'''

# Examples: check "Use_module.py"
def price(people):
    print("The price for {0} people is It's ${1}."\
        .format(people,people*10))

def price_morning(people):
    print("The price of morning for {0} people is It's ${1}."\
        .format(people,people*6))

def price_soldier(people):
    print("The price of soldier for {0} people is It's ${1}."\
        .format(people,people*4))
