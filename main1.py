def Addition(No1,No2):
    print("Inside Addition function")
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    print("Inside main function")
    print("Enter first number : ")   
    A = int(input()) 

    print("Enter first number : ")   
    B = int(input()) 

    Result = Addition(A,B)

    print("Addition is:",Result)

main()    
print("End of application")