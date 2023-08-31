# 카드2
from collections import deque

num = deque(range(1, int(input()) + 1))

while len(num) != 1:
    num.popleft()
    num.append(num.popleft())

print(num[0])
