import random
import math

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


def quaz(left, right, n):
    diff = (right - left) // n
    for i in range(n):
        a.append(i * diff + left + random.randint(0, diff * 2))


def bubble_sort(a):
    n = len(a)
    swap = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                swap = True
                a[j], a[j + 1] = a[j + 1], a[j]
            if not swap:
                return


def shell_sort(a):
    n = len(a)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = a[i]
            j = i
            while j > interval and a[j - interval] > temp:
                a[j] = a[j - interval]
                j -= interval
            a[j] = temp
        k -= 1
        interval = 2 ** k - 1


if __name__ == "__main__":
    quaz(1, 20, 5)
    print(a)
    shell_sort(a)
    print("Sorted array is:")
    for i in range(len(a)):
        print("% d" % a[i], end=" ")
