# Package: Collection of Modules
# Check travel/
# The module name must follow the import.
# Module name and Package can follow the From

# import (module)
'''
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
'''

# from (package or module) import (module or class)
'''
from travel import vietnam
trip_to = travel.vietnam.VietnamPackage()
trip_to.detail()
'''

# from (package or module) import * (* = all)
# if __init__.py don't have __all__ [list], you can't use this code
'''
from travel import *
trip_to = travel.vietnam.VietnamPackage()
trip_to.detail()
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
'''

