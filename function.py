

def sum():
    s= n1 + n2 
    print("Sum of",n1 ,"&",n2,"is",s)

def substract():
    a= n1-n2 
    print("Difference of",n1,"&",n2,"is",a)

def multiply():
    m= n1*n2 
    print("Multiplication of",n1,"&",n2,"is",m)

def division():
    d=n1/n2 
    print("Division of",n1,"&",n2,"is",d)


ans = 'y'
while ans == 'y':
   
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("                                                                     MAIN MENU                                                                    ")
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("                          1. Addition                                                                                                            ")
    print("                          2. Sunstraction                                                                                                        ")
    print("                          3. Multiplication                                                                                                      ")
    print("                          4. Division                                                                                                            ")
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
 
   
    c=int(input("Enter your choice (1-4) : "))
    n1=int(input("Enter 1st number : "))
    n2=int(input("Enter 2nd number : "))
    if c==1:
        sum()
    elif c==2 :
        substract()
    elif c==3 :
        multiply()
    elif c==4 :
        division()
    else:
        print("Invalid choice!! ")

    
    
    ans=input("Do you wish to continue (y/n) ? ")

else:
    print("THANK YOU FOR USING CALCLATOR")

   
   


 
