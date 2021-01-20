# Leave the empty space. Align Right(>) While Freeing 10 Digits
'''
print("{0: >10}".format(500))
'''

# Mark positive + negative as -
'''
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
'''

# Align Left, Fill in the blanks with _
'''
print("{0:_<10}".format(500))
'''

# every three digits display ','
'''
print("{0:,}".format(50000000000000))
print("{0:+,}".format(-50000000000000))
'''

# Decimal point output
'''
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))
'''