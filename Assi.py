def digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + digits(n // 10)

num = int(input("Enter a number: "))
result = digits(num)
print(f"The sum of digits of {num} is {result}")