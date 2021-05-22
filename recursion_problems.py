# 1. Sum of n numbers
def find_sum(n):
    if n==1:
        return 1;
    return n + find_sum(n-1)
#2. Fibonacci Series
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(6))
    print(find_sum(7))

