#Program to count the no. of vowels in story.txt
f=open("story.txt")
contents=f.read()
print(contents)
print("----------------------------------------------------------")
vowel=0
for ch in contents :
    if ch in ['a','e','i','o','u'] :
        vowel+=1
print("No. of vowels are : ",vowel)
f.close()



#Program to count the no. of words in story.txt
f=open("story.txt")
contents=f.read()
print(contents)
print("----------------------------------------------------------")
wc=0
wordsList=contents.split()
print(wordsList)
print("----------------------------------------------------------")
for eachword in wordsList :
    wc+=1
print("No of words are : ", wc)
f.close()



#Program to count the no. of lines in story.txt
f=open("story.txt")
contents=f.read()
print(contents)
print("----------------------------------------------------------")
lc=0
Line=contents.splitlines()
print(Line)
for eachline in Line :
    print(eachline)
    lc+=1
print("No. of lines are : ",lc)
f.close()





