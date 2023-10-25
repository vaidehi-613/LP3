def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Replace `n` with the term number you want in the Fibonacci series
n = 10
result = [fibonacci_recursive(i) for i in range(n)]
print(result)