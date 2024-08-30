# Python program to print the Fibonacci series up to n terms

# Function to print Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Number of terms
num_terms = 10  # You can change this value for a different result

# Print the Fibonacci series
fibonacci(num_terms)

