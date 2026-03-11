import sys
from time import time
import random


# You will need to implement this function and change the return value.
def mod_exp(x: int, y: int, N: int) -> int:
    #Base Case
    if y == 0:
        return 1

    #Recursion
    z = mod_exp(x, y//2, N)

    if y % 2 == 0:
        return (z*z) % N
    else:
        return (x*z*z) % N


def fermat(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """
    if N <= 1:
        return False
    if N <= 3:
        return False

    for _ in range(k):
        a = random.randrange(2, N)

        if mod_exp(a, N-1, N) != 1:
            return False
    return True


def miller_rabin(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """
    return False


def generate_large_prime(n_bits: int) -> int:
    """Generate a random prime number with the specified bit length"""
    while True:
        a = random.getrandbits(n_bits)
        a |= (1 << (n_bits - 1))
        a |= 1

        if fermat(a, 20):
            return a

def main(n_bits: int):
    start = time()
    large_prime = generate_large_prime(n_bits)
    print(large_prime)
    print(f'Generation took {time() - start} seconds')


if __name__ == '__main__':
    main(int(sys.argv[1]))
