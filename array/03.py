def solution(arr):
    # 정답 리스트 선언
    res = []
    # 인덱스 0부터 마지막 인덱스 까지 합 반복 -> 리스트에 담기
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            res.append(arr[i] + arr[j])
    # 중복 제거 하고 정렬
    return sorted(set(res))


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
