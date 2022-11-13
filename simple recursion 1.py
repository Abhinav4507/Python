#simple recursion 1 
# program which calculate the power of any munber to any base using recursion

def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)

#_____main____
print("Enter only positive numbers below")
num=int(input("Enter base number : "))
p=int(input("Raised to power of : "))
result=power(num,p)
print(num,"Raised to power of ",p,"is",result)
