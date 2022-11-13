
def Asciivalue(ch) :
    print("ASCII value of ",ch,"is",ord(ch))

ans='Y'
while ans.upper()=='Y':
    ch=input("Enter any single charcter : ")
    Asciivalue(ch)
    ans=input("wish to continue ")

#----------EXPLAIN EACH LINE OF CODE
def toUppercase(s):
    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    for x in s :
        if x not in alphabet or alphabet.index(x)>=26:
            result+=x
        else :
            result+=alphabet[alphabet.index(x)+26]
    print(result)
text=input("Enter any text : ")
toUppercase(text)
