import sys
from time import time
from math import gcd

from prime_number_generation import generate_large_prime, mod_exp

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
# If none of these work, throw an exception (and let the instructors know!)
primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]

def ext_euclid(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return 1, 0, a
    x, y, z = ext_euclid(b, a % b)
    return y, x - (a // b) * y,z

def generate_key_pairs(n_bits) -> tuple[int, int, int]:
    p = generate_large_prime(n_bits)
    q = generate_large_prime(n_bits)

    N = p*q
    e = None
    prod = (p-1)*(q-1)

    for i in primes:
        if gcd(i, prod) == 1:
            e = i
            break

    if e is None:
        raise Exception('No primes found')

    #Euclids algorythm
    _, d, g = ext_euclid(prod, e)

    d = d % prod

    return N, e, d


def main(n_bits: int, filename_stem: str):
    start = time()
    N, e, d = generate_key_pairs(n_bits)
    print(f'{time() - start} seconds elapsed')

    public_file = filename_stem + '.public.txt'
    with open(public_file, 'w') as file:
        file.writelines([
            str(N),
            '\n',
            str(e)
        ])
    print(public_file, 'written')

    private_file = filename_stem + '.private.txt'
    with open(private_file, 'w') as file:
        file.writelines([
            str(N),
            '\n',
            str(d)
        ])
    print(private_file, 'written')


if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2])
