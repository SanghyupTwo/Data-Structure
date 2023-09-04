# 방 배정

import math

n, k = map(int, input().split())
arr = [[0] * 2 for _ in range(6)]  # 성별2개 6학년
cnt = 0

# 입력
for _ in range(n):
    # st[학년][성별]
    s, y = map(int, input().split())
    arr[y - 1][s] += 1

for i in range(6):
    for j in range(2):
        if arr[i][j] == 0:
            continue
        elif arr[i][j] <= k:
            cnt += 1
        else:
            # 이 부분을 math.ceil(arr[i][j]//k)로 해서 올림을 제대로 하지 못했음
            cnt += math.ceil(arr[i][j] / k)
'''
for i in arr:
    for j in i:
        cnt += math.ceil(j/k)
'''
print(cnt)
