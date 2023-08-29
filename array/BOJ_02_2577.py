# 숫자의 개수
import sys

input = sys.stdin.readline
n = int(input()) * int(input()) * int(input())
num = [0] * 10

for i in str(n):
    num[int(i)] += 1

print(*num, sep='\n')
