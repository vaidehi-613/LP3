def fibonacci(n):
    fib_series = []
    
    a, b = 0, 1
    count = 0

    while count < n:
        fib_series.append(a)
        a, b = b, a + b
        count += 1

    return fib_series

# Replace `n` with the number of terms you want in the Fibonacci series
n = 10
result = fibonacci(n)
print(result)