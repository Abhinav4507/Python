#simple recursion
#program which reverse the direction of string using recursion

def bp(sg,n):
    if n>0 :
        print(sg[n],end='')
        bp(sg,n-1)
    elif n==0 :
        print(sg[0])

#-----------main--------------
s=input("Enter any string : ")
bp(s,len(s)-1)

