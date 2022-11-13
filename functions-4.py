#Function to swap the value of 2 variables
n1=10
n2=20
def swap () :
    global n1,n2
    n1,n2=n2,n1
    print("within swap() :")
    print("n1=",n1,"n2=",n2)

#----main-----
print("within main before calling swap() :")
print("n1=",n1,"n2=",n2)
swap()
print("within main after calling swap ():")
print("n1=",n1,"n2=",n2)




#Use of global keyword
s="Good Morning"
def f():
    global s
    s=" CS Class"
    print("within function :",s)

#---main---
print("within main before calling f() :",s)
f()
print("within main after calling f() : ",s)





#Passing list as an argument to a function
def sumList (L) :
    s=0
    for ele in L :
        s+=ele
        print(ele)
    print("Sum of list elements = ",s)

#--main----

L=[1,2,3,4,5,6]
sumList(L)    












