import math


def main():
    while True:
        try:
            n = int(input("Enter a positive integer: "))
        except ValueError:
            continue
        else:
            if n > 0:
                break

    factors = prime_factors(int(n))
    print(f"The prime factors of {n} are {factors}")


def prime_factors(n):
    """Find the prime factors of any positive integer"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(int(i))
            n /= i
    if n > 2:
        factors.append(int(n))
    return factors


main()
