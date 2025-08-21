#fibonacci
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b



n=int(input("Enter the range of the fibonacci series : "))
fibonacci_series(n)