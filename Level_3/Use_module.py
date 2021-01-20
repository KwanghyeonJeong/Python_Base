# import module
'''
import theather_module
theather_module.price(3)
theather_module.price_morning(4)
theather_module.price_soldier(5)
'''

# you can use theather_module as "mv"
'''
import theather_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)
'''

# you can use everything in the module.
'''
from theather_module import *
price(3)
price_morning(4)
price_soldier(5)
'''

# you can use price and price_morning in the module.
'''
from theather_module import price, price_morning
price(5)
price_morning(6)
'''
# you can use price_soldier as "ps" in the module.
'''
from theather_module import price_soldier as ps
ps(8)
'''
