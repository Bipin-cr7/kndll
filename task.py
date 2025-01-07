def Calculator():
    while True:
        print("  ----------- CALCULATOR ---------------")
        num1= float(input("Enter first number : "))
        num2= float(input("Enter second  number : "))

        print("1 for addition  ")
        print("2 for subraction  ")
        print("3 for multiplication  ")
        print("4 for division  ")
        Choice =int(input("Enter your choice "))

    
        if Choice==1:
            
                    print(f"Sum of {num1} and {num2} is : {num1+num2}")
        
        
        if Choice==2:
            
                print(f"difference of {num1} and {num2} is : {num1-num2}")

        if Choice==3:
            
                print(f"product of {num1} and {num2} is : {num1*num2}") 

    
        if Choice==4:
        
                print(f"quotient of {num1} and {num2} is : {num1/num2}")
                
        playagain = input("Do you wana use calculator again : (yes/no) ")
        if playagain!="yes":
            print("Thank you for using have a great day")
            break
        

if __name__=="__main__":
       Calculator()
