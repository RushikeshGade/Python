import multiprocessing
import os

def EvenDisplay(No):
    print("PID of even process ",os.getpid())
    print("List of even number :")
    x = 2
    for i in range(No):
        print(x)
        x = x+2

def OddDisplay(No):
    print("PID of odd process ",os.getpid())
    print("List of odd number :")
    x = 1
    for i in range(No):
        print(x)
        x = x+2

def main():
    print("Enter number :")
    Value = int(input())

    p1 = multiprocessing.Process(target = EvenDisplay, args = (Value,))
    p2 = multiprocessing.Process(target = OddDisplay, args = (Value,))
     
    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print("End of main process")

    EvenDisplay(Value)
    OddDisplay(Value)

if __name__ == "__main__":
    main()  


