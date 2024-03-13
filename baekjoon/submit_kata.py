n = int(input())
row = [0] * n
ans = 0


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or (abs(row[x] - row[i]) == abs(x - i)):
            return False

    return True


def n_queen(x, n):
    global ans
    if x == n:
        ans += 1
        return

    # 위에서 아래로 퀸을 배치한다.
    for y in range(n):
        # [x,y]에 퀸을 배치한다는 뜻
        row[x] = y

        # 이전 queen(row[i, y])과 현재 queen(row[x,y])을 비교하여 동일 행, 대각선에 없으면 재귀적으로 배치한다.
        if is_promising(x):
            n_queen(x + 1, n)


n_queen(0, n)
print(ans)
