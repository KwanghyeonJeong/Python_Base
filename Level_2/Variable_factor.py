# *language:variable_factor
'''
def profile(name, age, *language):
    print("name: {0}\tage: {1}\t".format(name,age),end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("Steve",20,"Python","Java","C","C++","C#")
profile("John",25,"Kotlin","Swift","","","")
'''
