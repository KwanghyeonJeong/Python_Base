# continue and break

# absent student number
absent = [2,5]
# A student who didn't bring a book
no_book = [7]
for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue # skip this case(student in absent)
    elif student in no_book:
        break # break loop
    print("{0}, Read books.".format(student))



