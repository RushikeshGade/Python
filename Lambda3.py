# def Cube(A):
#     return A*A*A


# Add = lambda A : A*A*A

# def main():
#     Ret = Cube(10,11)
#     print("Cube is :" ,Ret)

# if __name__ == "__main__":
#     main()    

# or

# Name = lambda Parameters : Logic
# Name(___, ___, .....)

def Cube(A):
    return A*A*A

CubeX = lambda A : A*A*A

def main():
    Ret = CubeX(10)
    print("Cube is : ",Ret)

if __name__ == "__main__":
    main()