# Functions
def Double(num):
    print("Double of",num,"is",num*2)

def Square(num):
    print("Square of",num,"is",num**2)

def Cube(num) :
    print("Cube of",num,"is",num**3)

#-------------Main program-------------------
print("------------------MAIN MENU--------------------")
print("     1. Double of any number " )
print("     2.Square of any number ")
print("     3.Cube of any number " )
print("------------------------------------------------------")

ans='y'
while ans=='y':
    choice=int(input("Enter your choice : "))
    num=int(input("Enter the number : "))
    if choice==1:
        Double(num)
    elif choice==2:
        Square(num)
    elif choice==3:
        Cube(num)
    else:
        print("Invalid choice....valid choice is from 1-3")
    ans=input("Do you wish to continue....y/n ")

    
