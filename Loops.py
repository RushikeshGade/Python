
def DisplayF():
    print("inside display of for loop")
    for i in range(1,6):
        print(i)
        
def DisplayW():
    print("inside display of while loop")    
    no = 1
    while(no <= 5):
        print(no)
        no = no +    1

def main():
    DisplayF()
    DisplayW()

if __name__ == "__main__":
    main()