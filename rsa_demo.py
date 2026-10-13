"""Educational RSA demonstration. NOT for real-world secure encryption."""
from __future__ import annotations
import argparse
import math
import secrets
import time


def is_probable_prime(n: int, rounds: int = 24) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n == p:
            return True
        if n % p == 0:
            return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(rounds):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_prime(bits: int) -> int:
    while True:
        x = secrets.randbits(bits) | (1 << (bits - 1)) | 1
        if is_probable_prime(x):
            return x


def generate_keys(bits: int = 512) -> tuple[tuple[int, int], tuple[int, int]]:
    if bits < 32:
        raise ValueError('Key size must be at least 32 bits for this demo.')
    e = 65537
    while True:
        p, q = generate_prime(bits // 2), generate_prime(bits - bits // 2)
        if p == q:
            continue
        phi = (p - 1) * (q - 1)
        if math.gcd(e, phi) == 1:
            n = p * q
            d = pow(e, -1, phi)
            return (n, e), (n, d)


def encrypt(message: str, public_key: tuple[int, int]) -> list[int]:
    n, e = public_key
    return [pow(b, e, n) for b in message.encode('utf-8')]


def decrypt(ciphertext: list[int], private_key: tuple[int, int]) -> str:
    n, d = private_key
    raw = bytes(pow(c, d, n) for c in ciphertext)
    return raw.decode('utf-8')


def main() -> None:
    parser = argparse.ArgumentParser(description='Educational RSA demo (textbook RSA, insecure).')
    parser.add_argument('--message', default='Xin chào RSA!')
    parser.add_argument('--bits', type=int, default=512)
    args = parser.parse_args()
    print('RSA DEMO — educational only; no OAEP padding, NOT secure for production')
    t0 = time.perf_counter()
    public, private = generate_keys(args.bits)
    t1 = time.perf_counter()
    ciphertext = encrypt(args.message, public)
    t2 = time.perf_counter()
    recovered = decrypt(ciphertext, private)
    t3 = time.perf_counter()
    print(f'Public key: (n={public[0]}, e={public[1]})')
    print(f'Private exponent d (demo only): {private[1]}')
    print(f'Original: {args.message}')
    print(f'Ciphertext (one integer per UTF-8 byte): {ciphertext}')
    print(f'Decrypted: {recovered}')
    print(f'Correct: {recovered == args.message}')
    print(f'Time (keygen/encrypt/decrypt): {t1-t0:.4f}s / {t2-t1:.4f}s / {t3-t2:.4f}s')


if __name__ == '__main__':
    main()
