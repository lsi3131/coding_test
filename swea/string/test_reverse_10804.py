# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PyTLqAf4DFAUq

'''
테스트 데이터
2
bdppq
qqqqpppbbd
'''

def solution(s: str):
    word_dict = {
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p',
    }
    s_reverse = []
    for ch in s:
        s_reverse.append(word_dict[ch])
    return ''.join(s_reverse)[::-1]

# ---- submit ----

T = int(input())

for test_case in range(1, T + 1):
    s = input()

    result = solution(s)
    print(f'#{test_case} {result}')
