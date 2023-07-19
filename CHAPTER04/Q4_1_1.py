def fib(n):
    """nより小さなフィナボッチ数列を列挙する"""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
