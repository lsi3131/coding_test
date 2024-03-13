memo = [0, 1]


def fib(n):
    if n < len(memo):
        return n

    memo.append(fib(n - 1) + fib(n - 2))
    return memo[n]


'''
memoization. 계산했던 녀석 미리 등록해둠
Top-Down 방식

'''
print(fib(1000))
