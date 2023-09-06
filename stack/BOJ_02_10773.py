# 제로
import sys

input = sys.stdin.readline

stack = [0]
for _ in range(int(input())):
    num = int(input())
    # 한 줄로 가능
    # stack.pop() if num == 0 else stack.insert(num)
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
