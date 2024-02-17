def solution(arr):
    arr.sort()
    return arr


# return에서 바로 arr.sort()를 하면 None이 출력
# return에 바로 하려면 sorted(arr) 사용

print(solution([1, -5, 2, 4, 3]))
