def Display(Cnt):
    i = 0

    if(Cnt <=0):
        print("Invalid input")
        return

    while(i < Cnt):
        print("Jay Ganesh",end=" ")


def main():
    print("please entre the frequenct:")
    No = int(input())
    Display(No)

if__name__ == "__main__":
   main()