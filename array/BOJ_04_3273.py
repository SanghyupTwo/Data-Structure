# 두 수의 합
n = input()
arr = set(map(int, input().split()))
x = int(input())
ans = 0
# set의 in 연산으로 문제 풀기
for i in arr:
    # set의 in 연산의 시간 복잡도는 O(1)이다.
    if x - i in arr:
        ans += 1

# 쌍의 개수를 출력해야 되니까 2로 나누어 준다.
print(ans // 2)

# 투 포인터를 이용해서 문제 풀기
# arr 리스트를 정렬 해줘야 된다.
ans = 0
left, right = 0, n - 1  # 왼쪽, 오른쪽
while left < right:
    temp = arr[left] + arr[right]
    if temp == x:
        ans += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(ans)

'''
set을 sorted()를 이용해서 정렬하면 리스트로 반환힌다.
list의 in 연산은 시간복잡도가 O(N)이라서 시간 초과가 발생한다.
'''
