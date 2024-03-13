'''
()(((()())(())()))(())

(((()(()()))(())()))(()())
'''


def solution(s: str):
    count = 0
    stack = []
    i = 0
    while i < len(s):
        # 레이저 인경우
        if (i + 1) <= len(s) - 1 and s[i] == '(' and s[i + 1] == ')':
            if stack:
                count += len(stack)
            i += 2
        # 일반 stick
        else:
            if s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                stack.pop()
                count += 1
            i += 1

    return count


s = input()
print(solution(s))
