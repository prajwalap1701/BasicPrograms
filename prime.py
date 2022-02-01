while True:
    n = int(input("Enter a number: "))

    if n==2 or n==3 or n==5 or n==7:
        print("Prime number")
    elif n==1 or n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0:
        print("Composite number")
    else:
        print("Prime number")