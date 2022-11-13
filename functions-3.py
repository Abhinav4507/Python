def Sum(n1,n2,n3):
    s=n1+n2+n3
    return s

#---------returning multiple values
def Calculate(x,y):
    print("x=",x,"y=",y)
    return x+y, x-y, x*y, x/y, x%y

#------------------------------------

def Increment(x):
    x+=1
    print(x)

#--------main-----------
print(Sum(10,2,90))
res=Sum(10,20,50)
print(res)
print("Sum is ",res,"Average is", res/3)


print()
print(Calculate(100,10))
sum,sub,prod,quo,mod=Calculate(100,3)
print(sum,sub,prod,quo,mod)

print()
x=3
print(x)
Increment(x)
print(x)
