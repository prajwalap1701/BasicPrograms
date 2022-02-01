def fib_recursion(n):
    print(n)
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)

def fib(n):
    n1 =0
    n2 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return '1 1'
    else:
        count = 0
        fib_n = 0
        while count < n+1:
            print(n1)
            fib_n = n1 + n2
            n1 = n2
            n2 = fib_n

            count += 1


# print(fib_recursion(4))
print(fib(7))