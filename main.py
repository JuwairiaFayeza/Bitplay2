# def checknumber(number1,number2):
#     if ((number1^number2)!=0):
#         print("Number are not equal")
#     else:
#         print("numbers are equal")
# number1=int (input("enter number1===="))
# number2=int (input("enter number2===="))

# checknumber (number1,number2)

#activity 2

def oddocuring(arr):
    res=0
    for element in arr :
       res = res ^ element
    return res 
arr= []
n= int(input("enter arr sign"))
while(n):
    num= int(input("enter number"))
    arr.append(num)
    n-=1
print("odd number is", oddocuring(arr))