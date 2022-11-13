#Default arguments

def simpleInterest(P,R,T=12):
    print(P,R,T,sep="-------")
    si=(P*R*T)/100
    print("Simple interest is",si)

#-----------variable length argument
def Sum(*num):
    s=0
    for i in num :
        s+=i
    print("Sum is",s)

#----main-----------------------------

simpleInterest(5000,10,12)              #postional arguments
simpleInterest(5000,10,24)
simpleInterest(5000,10)                       #default argument

simpleInterest(R=10,T=24,P=5000)   #keyword/named argument

simpleInterest(10,24,5000)              #postional arguments

print()
Sum(1,2)
Sum(1,2,3,4,5)
Sum(1,2,3,4,5,6,7,8)







        
