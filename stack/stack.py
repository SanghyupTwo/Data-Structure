# 파이썬으로 스택 구현
stack = []


# Push 연산 구현
def push(x):
    stack.append(x)


# Pop 연산 구현
def pop():
    if not is_empty():
        stack.pop()


# Top 연산 구현
def top():
    if not is_empty():
        return stack[-1]


# Is_Empty 연산 구현
def is_empty():
    return len(stack) == 0


# test 함수 구현
def test():
    push(5)  # [5]
    push(4)  # [5, 4]
    push(3)  # [5, 4, 3]
    print(top())  # 3
    pop()  # [5, 4]
    pop()  # [5]
    print(top())  # 5
    push(10)  # [5, 10]
    push(12)  # [5, 10, 12]
    print(top())  # 12
    pop()  # [5, 10]
    print(top())  # 10


# main 함수
def main():
    test()


if __name__ == "__main__":
    main()
