def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        print(a, sep=' ', end=' ' if i < n - 1 else '\n')
        a += b
        b = a - b


def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)


n = int(input())
print("{n} Digit of Fibonacci : ", end='')
fibonacci(n)
print("Factorial of {n} : ", end='')
print(factorial(n))
