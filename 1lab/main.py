import random
import math
import time

a = []


def rand(left, right, n):
    for i in range(n):
        a.append(random.randint(left, right))


def randN(left, right, n):
    for i in range(0, n):
        a.append(int((right - left) * i / n + left))


def revRandN(left, right, n):
    for i in range(0, n):
        a.append(int((right - left) * i / n + left))
    a.reverse()


def interSaw(left, right, n, k):
    interval = math.ceil(n / k)
    for i in range(0, n):
        a.append(int((right - left) * (i % interval) / interval + left))


def interSin(left, right, n, k):
    interval = math.ceil(n / k)
    for i in range(0, n):
        a.append(int((right - left) * abs(math.cos((i % (interval + 1)) / interval * math.pi)) + left))


def quaz(left, right, n):
    diff = (right - left) // n
    for i in range(n):
        a.append(i * diff + left + random.randint(0, diff * 2))


def step(left, right, n, k):  # values between steps can be more or less than i step, but not more than i + 1 step.
    interval = n / k
    delta = (right - left) // k
    for i in range(0, k):
        for j in range(0, int(interval)):
            a.append(delta * i + random.randint(0, delta))


if __name__ == "__main__":
    for n in range(500000, 5000001, 500000):
        start = time.time()
        quaz(1, 10000000, n)
        stop = time.time()
        print(f'{stop - start:2f}')
        a = []
        rand(1, 100000, n)
