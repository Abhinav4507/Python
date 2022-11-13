
f=open("story.txt")
contents=f.read()
print("The contents of file are ")
print(contents)
f.close()


f=open("story.txt")
contents=f.read(10)
print(contents)
contents=f.read(17)
print(contents)
f.close()


f=open("story.txt")
print(f.closed)
print(f.encoding)
print(f.mode)
print(f.newlines)
print(f.name)



