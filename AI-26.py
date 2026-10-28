number = int(input("Enter a whole number: "))

if number < 2:
    print("Not a prime number")
else:
    divisor = 2

    while divisor * divisor <= number and number % divisor != 0:
        divisor += 1

    if divisor * divisor > number:
        print("Prime number")
    else:
        print("Not a prime number")
