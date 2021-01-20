# define function
def profile(name,age,main_lang):
    # '\' => can write code at next line
    print("name: {0}\t age: {1}\t lang: {2}"\
        .format(name,age,main_lang))

'''
profile("steve",20,"Python")
profile("Tom",25,"Java")
'''

# basic_value

def profile2(name,age=17,main_lang="Python"):
    print("name: {0}\t age: {1}\t lang: {2}"\
        .format(name,age,main_lang))


'''
profile2("steve")
profile2("Ellen")
'''