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
        a.insert(0, int((right - left) * i / n + left))


def interSaw(left, right, n, k):
    interval = math.ceil(n / k)
    for i in range(0, n):
        a.append(int((right - left) * (i % interval) / interval + left))


def interSin(left, right, n, k):
    interval = math.ceil(n / k)
    for i in range(0, n):
        a.append(int((right - left) * abs(math.cos((i % (interval + 1)) / interval * math.pi)) + left))


def step(left, right, n, k):  # values between steps can be more or less than i step, but not more than i + 1 step.
    # let's say that every step divided by 5
    interval = math.ceil(n / k)


# def quazStep(left, right, n, k):
#     interval = math.ceil(n / k)
#     for i in range(0, n):
#         if i % 5 != 0:
#             a.append(random.randint(i // 5, (i // 5) + 5))
#         else:
#             a.append(i / 5)

if __name__ == "__main__":
    # for n in range(500000, 5000001, 500000):
    #     start = time.time()
    #     interSin(1, 10000000, n, 50000)
    #     stop = time.time()
    #     print(f'{n} - {stop - start}')
    #     a = []
    print(a)
