# https://www.acmicpc.net/problem/1759

'''
4 6
a t c i s w

5 6
a i e s o k
'''


def solution(s_list, l):
    s = ''.join(sorted(s_list))
    vowels = 'aeiou'
    results = []

    def dfs(path, start, vowel_count, l):
        # 최소 2개 이상의 자음을 위한 처리
        # 자음 길이 = 문자열 개수 - 모음 개수
        if not ((l - vowel_count) >= 2):
            return

        if len(path) == l:
            # 모음이 최소 1개 이상 필요
            if vowel_count >= 1:
                results.append(path)

        for i in range(start, len(s)):
            next_vowel_count = vowel_count
            if s[i] in vowels:
                next_vowel_count += 1
            dfs(path + s[i], i + 1, next_vowel_count, l)

    dfs('', 0, 0, l)
    return results


l, c = map(int, input().split())
s_list = input().split()
results = solution(s_list, l)
for r in results:
    print(r)
