#Return statement and Memory environment
def Sum(a,b,c) :
    s=a+b+c
    return s
def Average(x,y,z) :
    sm=Sum(x,y,z)
    return sm/3

#---main------
n1=int(input("Enter number : "))
n2=int(input("Enter number : "))
n3=int(input("Enter number : "))
print("Average is : ",Average(n1,n2,n3))




#Mutable value passed to the function
def myfunct2(myList) :
    print("In function - list : ",myList)
    myList[0]+=2
    print("List changed : ",myList)
    return

List1=[1,2]
print("Before calling function :" ,List1)
myfunct2(List1)
print("After calling function : " ,List1)






          
