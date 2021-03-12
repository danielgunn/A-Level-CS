lines = '''this is the first line
this is line 2
this is line 3
this is the last line'''
f = open("foo.txt", "w")
f.writelines(lines)
f.close()

fo = open("foo.txt", "r")
line = fo.readline()
print("Read Line:",line,end='')
# Seek to the second character first line
fo.seek(1, 0)
line = fo.readline()
print("Read Line:",line,end='')
fo.close()