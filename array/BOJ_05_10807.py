# 개수 세기
n = input()
num = list(map(int, input().split()))
v = int(input())
# count() 이용해서 문제 풀기
print(num.count(v))

# 배열의 인덱스 이용해서 문제 풀기
arr = [0] * 201

for i in num:
    arr[i] += 1

print(arr[v])
