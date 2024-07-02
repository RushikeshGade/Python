print("Demontration of Procedural")

def Addition(No1, No2):
    Ans = No1 + No2
    return Ans

def Substraction(No1, No2):
    Ans = No1 - No2
    return Ans

def main():
    print("Enter first number")
    A= int(input()) 

    print("Enter second number")
    B= int(input())

    Ret = Addition(A,B)
    print("Addition is ",Ret)

    Ret = Substraction(A,B)
    print("Substraction is ",Ret)

if __name__ =="__main__":
    main()    