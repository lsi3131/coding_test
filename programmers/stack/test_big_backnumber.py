def solution(numbers):
    results = [-1] * len(numbers)

    st = []
    for i, n in enumerate(numbers):
        while st and numbers[st[-1]] < n:
            results[st.pop()] = n
        st.append(i)

    return results


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
