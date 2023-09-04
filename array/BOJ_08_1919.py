# 애너그램 만들기

arr = [0] * 26

# 첫 번째 문자열을 입력 받고, 각 문자의 빈도수를 배열에 저장
for s in list(input()):
    arr[ord(s) - 97] += 1

# 두 번째 문자열을 입력 받고, 각 문자의 빈도수를 배열에서 감소
for s in list(input()):
    arr[ord(s) - 97] -= 1

# 배열의 모든 요소의 절대값을 더하여 필요한 작업 횟수 계산
print(sum(map(abs, arr)))  # 배열의 각 요소의 절대값을 더함
