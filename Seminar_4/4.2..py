def factorial(n):
    n = int(float(n))
    if n < 1:
        return -1
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


number = input('Your number: ')
print(factorial(number))