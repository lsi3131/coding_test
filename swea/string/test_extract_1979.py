# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq

'''
2
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
'''


# 가로, 세로 순회할 때 중복이 너무 심하다. 줄일 수 있는 방안이 있는지 검토한다.

def solution(mat, k):
    # 가로, 세로로 순회하여 비어있는 공간을 계산하여 list에 저장한다.
    # 가로 순회
    space_length_list = []
    for row in range(len(mat)):
        space_length = 0
        for col in range(len(mat[row])):
            if mat[row][col] == 1:
                space_length += 1
            else:
                if space_length > 0:
                    space_length_list.append(space_length)
                space_length = 0
        if space_length > 0:
            space_length_list.append(space_length)

    # 세로 순회
    for col in range(len(mat[0])):
        space_length = 0
        for row in range(len(mat[col])):
            if mat[row][col] == 1:
                space_length += 1
            else:
                if space_length > 0:
                    space_length_list.append(space_length)
                space_length = 0
        if space_length > 0:
            space_length_list.append(space_length)

    result_space = [s for s in space_length_list if s == k]
    return len(result_space)


# --- submit ----
T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    mat = []
    for _ in range(n):
        row = list(map(int, input().split()))
        mat.append(row)

    result = solution(mat, k)
    print(f'#{test_case} {result}')
