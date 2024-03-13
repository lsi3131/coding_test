n = int(input())

fib1_count = 0
fib2_count = 0


def fib1(n):
    global fib1_count
    if n <= 2:
        fib1_count += 1
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    global fib2_count
    fibs = [0, 1]
    if n <= 2:
        return 1

    for i in range(2, n):
        fibs.append(fibs[i - 1] + fibs[i - 2])
        fib2_count += 1

    return fibs[-1]


fib1(n)
fib2(n)

print(f'{fib1_count} {fib2_count}')
