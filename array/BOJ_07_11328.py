# Strfry
import sys

input = sys.stdin.readline

for i in range(int(input())):
    a, b = input().rstrip().split()
    # 두 문자열을 정렬한 결과가 같으면 알파벳의 개수가 같은 것
    if sorted(a) == sorted(b):
        print("Possible")
    else:
        print("Impossible")

# 알파벳 리스트를 이용해서 풀기
for _ in range(N):
    a = [0] * 26  # 각 문자의 개수를 저장하는 리스트
    s1, s2 = input().split()

    for c in s1:
        a[ord(c) - ord('a')] += 1  # 첫 번째 문자열의 각 문자는 개수+1
    for c in s2:
        a[ord(c) - ord('a')] -= 1  # 두 번째 문자열의 각 문자는 개수-1

    # 0이 아닌 리스트의 요소가 있을 경우, 개수가 다른 문자가 존재하므로 False
    is_possible = all(count == 0 for count in a)

    if is_possible:
        print("Possible")
    else:
        print("Impossible")
