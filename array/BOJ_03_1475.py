# 방 번호
import sys

num = [0] * 10
ans = 0

for i in sys.stdin.readline().rstrip():
    num[int(i)] += 1

for i in range(10):
    if i == 6 or i == 9:
        continue
    else:
        ans = max(ans, num[i])

print(max(ans, (num[6] + num[9] + 1) // 2))
