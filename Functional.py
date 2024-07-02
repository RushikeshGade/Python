
print("Demontration of Functional")

Addition = lambda No1, No2 : No1 + No2

Substraction = lambda No1, No2 : No1 - No2
    
print("Enter first number")
A= int(input()) 

print("Enter second number")
B= int(input())

Ret = Addition(A,B)
print("Addition is ",Ret)

Ret = Substraction(A,B)
print("Substraction is ",Ret)
