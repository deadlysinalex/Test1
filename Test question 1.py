n=int(input("Enter a year"))
def leap():
    if(n == 1800):
        print("Not a leap year")
    elif(n == 1900):
        print("not a leap year")
    elif n%4==0:
        print("it is a leap year")
    elif n%100==0:
        if n%400==0:
            print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is not a leap year")

leap()
        
                




