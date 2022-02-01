def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(1,num+1):
            fact *= i

    return fact

def combination(n, r):
    return factorial(n)/(factorial(n-r) * factorial(r))

def permutations(n, r):
    return factorial(n)/factorial(n-r)

print(permutations(7, 2))
print(combination(7, 2))