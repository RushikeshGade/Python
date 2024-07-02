from functools import reduce

CheckEven = lambda No : (No % 2 == 0)

Increase = lambda No : No+1

Add = lambda A,B : A+B

def main():
    Data = [11,14,20,23,18,16,15,20]
    print("Data form inoput list : ",Data)

    FData = list(filter(CheckEven,Data))
    print("Dataafter filter activity :",FData)

    MData = list(map(Increase,FData))
    print("Data after map activity : ",MData)

    RData = reduce(Add,MData)
    print("Dta after reduce activity is :",RData)

if __name__ == "__main__":
    main()   