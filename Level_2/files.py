# open file "score.txt" Option: write You can use korean (utf8)
'''
score_file = open("score.txt",'w',encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 0", file=score_file)
score_file.close()
'''

# open file "score.txt" Option: append You can use korean (utf8)
'''
score_file = open("score.txt",'a',encoding="utf8")
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()
'''

# open file "score.txt" Option: read You can use korean (utf8)
'''
score_file = open("score.txt",'r',encoding="utf8")
# read all
print(score_file.read())
# read one line and Cursors move to next line.
print(score_file.readline())
# if you don't know how many lines in file
while True:
    line = score_file.readline()
    if not line:
        break;
    print(line)
score_file.close()
'''


