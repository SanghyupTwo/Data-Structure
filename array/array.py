# 새로운 요소를 배열의 특정 인덱스에 삽입하는 함수
def insert(idx, num, arr):
    global length
    arr.append(None)  # 배열 끝에 None 추가
    # 배열의 뒤에서부터 idx까지 요소들을 한 칸씩 뒤로 이동
    for i in range(len(arr) - 1, idx, -1):
        arr[i] = arr[i - 1]
    arr[idx] = num  # 지정한 인덱스에 새로운 요소 삽입
    length += 1  # 배열의 길이 증가
    print(arr, length)  # 결과 출력


# 배열에서 특정 인덱스의 요소를 삭제하는 함수
def erase(idx, arr):
    global length  # 글로벌 변수 'length'를 사용
    # idx부터 배열의 뒤에서 두 번째 요소까지 요소들을 한 칸씩 앞으로 이동
    for i in range(idx, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()  # 배열의 마지막 요소 제거
    length -= 1  # 배열의 길이 감소
    print(arr, length)  # 결과 출력


# 초기 배열과 길이 설정
arr = [10, 50, 40, 30, 70, 20]
length = 6

# 삽입 및 삭제 테스트
print("***** insert test *****")
insert(3, 60, arr)  # 10 50 40 60 30 70 20

print("***** erase test *****")
erase(4, arr)  # 10 50 40 60 70 20
