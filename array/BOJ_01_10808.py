# 알파벳 개수
import sys

input = sys.stdin.readline

# 딕셔너리를 이용해서 알파벳 개수 세기
abc = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
       'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, }
str_ = input().rstrip()
for i in str_:
    abc[i] += 1

print(*abc.values())

# 배열을 이용해서 알파벳 개수 세기
abc = [0] * 26
for s in sys.stdin.readline().rstrip():
    abc[ord(s) - ord('a')] += 1

print(*abc)
