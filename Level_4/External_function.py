# You can serch "list of python modules" on google.
# or access https://docs.python.org/ko/3/py-modindex.html

# glob : (= window dir)
'''
import glob
print(glob.glob("*.py"))
'''

# os : Basic features provided by the operating system
'''
import os
print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder):
    print("Already exist")
    os.rmdir(folder)
    print("remove dir")
else:
    os.makedirs(folder)
    print(folder, "mkdir")
print(os.listdir())
'''

# time
'''
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
'''

# datetime
'''
import datetime
print("Today is", datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days=100) # timedelta = Date Interval
print("100 days since we met is", today + td)
'''
