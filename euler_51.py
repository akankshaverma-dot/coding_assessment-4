from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def solve():
    num = 11

    while True:
        if is_prime(num):
            s = str(num)
            length = len(s)

            # Try replacing different positions
            for r in range(1, length):
                for positions in combinations(range(length), r):

                    family = []

                    for digit in '0123456789':
                        chars = list(s)

                        for pos in positions:
                            chars[pos] = digit

                        # Skip leading zero numbers
                        if chars[0] == '0':
                            continue

                        candidate = int(''.join(chars))

                        if is_prime(candidate):
                            family.append(candidate)

                    if len(family) == 8:
                        return min(family)

        num += 2 


print(solve())