# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PyTLqAf4DFAUq

def solution(s: str):
    return 1 if s == s[::-1] else 0


T = int(input())
for test_case in range(1, T + 1):
    s = input()

    result = solution(s)
    print(f'#{test_case} {result}')
