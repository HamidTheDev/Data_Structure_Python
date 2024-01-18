from ComplexityAnalyser.Analyser.

def fibonacci(n):
    fib = [0] * (n + 1)  # array filled with 0 to store Fibonacci numbers
    fib[1] = 1  # Set the base case f(1) = 1 and f(0) is already 0 by initialization

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]  # recurrence relation to calculate Fibonacci numbers

    return fib[n] #returning nth fibonacci number from the array

# Example usage
n = 30

# result, time_taken = ComplexityCalculator.measure_time(fibonacci(30))
# print(f"Result: {result}, Time: {time_taken} seconds")

result = fibonacci(n) # ans 3
print(f"The {n}th Fibonacci number is: {result}")
