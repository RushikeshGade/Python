import threading

def EvenDisplay(No):
    print("List of even number :")
    x = 2
    for i in range(No):
        print("Even :", x)
        x = x+2

def OddDisplay(No):
    print("List of odd number :")
    x = 1
    for i in range(No):
        print("Odd", x)
        x = x+2

def main():
    print("Enter number :")
    Value = int(input())

    

    p1 = threading.Thread(target = EvenDisplay, args = (Value,))
    p2 = threading.Thread(target = OddDisplay, args = (Value,))
     
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main process")

    EvenDisplay(Value)
    OddDisplay(Value)

if __name__ == "__main__":
    main()  


