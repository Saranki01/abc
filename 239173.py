def findmax(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2
    
num1= int (input("Enter  number 1:"))
num2= int (input("Enter  number 2:"))
num3= int (input("Enter  number 3:"))
num4= int (input("Enter  number 4:"))



max1= findmax(num1 ,num2)
max2= findmax(num3 ,num4)
print("Maximum of first two:" ,max1)
print("Maximum of first two:" ,max2)



