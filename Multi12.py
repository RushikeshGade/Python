import multiprocessing
import os
import time

def Fun(No):
    Sum  = 0
    print("PID is :",os.getpid())
    for i in range(No):
        Sum = Sum + (No*No*No)

    return Sum

def main():
    starttime = time.time()
    Arr = [100000,200000,300000,400000]
    Result = []

    

    p = multiprocessing.pool()
    Result = p.map(Fun,Arr)    
    p.close()
    p.join()

    print(Result)
    end=time.time()
    print("The requred for execution :",endtime-starttime)


if __name__ == "__main__":
    main()  
