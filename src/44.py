import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
    return factors

n = 128
if is_prime(n):
    print(f"{n} 是质数。")
else:
    factors = find_factors(n)
    if len(factors) == 2:
        print(f"两个不同的素因子是: {factors}")
    else:
        print("可能的质因数组合有多种，需要更多信息来确定。")

print("计算完成，请检查您的输入是否符合要求。")
