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

##fib non recursion
# time complexity : O(n) -> CUZ IT USES SIMPLE LOOP
# space complexity : O(1) -> cuz it uses constant amt of additional space to store only few variables.
