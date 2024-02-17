def solution(arr):
    unique_lst = list(set(arr))  # 중복값 제거
    unique_lst.sort(reverse=True)  # 내림차순 정렬
    return unique_lst
    # return sorted(set(arr), reverse=True) # 한 줄로 작성


print(solution([4, 2, 2, 1, 3, 4]))
