# 스택
import sys

input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    s = input().split()
    if s[0] == "push":
        stack.append(s[1])
    elif s[0] == 'pop':
        print(stack.pop() if len(stack) != 0 else -1)
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif s[0] == 'top':
        # 마지막 값을 확인 할 때 그냥 stack[-1]도 가능하다.
        print(stack[len(stack) - 1] if len(stack) != 0 else -1)
