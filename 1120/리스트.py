numbers = [25, 80, 30, 50, 11, 12]
machines = ["펌프", "모터", "압축기"]
mixed = [True, False, "문자열", 100, [1,2,3]]
print(numbers)
print(machines)
print(mixed)

### len(리스트) : 리스트의 요소 개수 확인
print(f'numbers의 요소 개수 확인 {len(numbers)}')
print(f'mixed의 요소 개수 확인 {len(mixed)}')
print(f'list의 요소 개수 확인 {len(["a", "b", "c"])}')
print(f'비어있는 리스트 요소 개수 확인 {len([])}') # 0

### 리스트의 인덱싱, 슬라이싱
# 슬라이싱: 결과값이 리스트, 원본 리스트를 변경하지 않음
numbers = [25, 80, 30, 50, 11, 12]
mixed = [True, False, "문자열", 100, [1,2,3]]
print(numbers[3])
print(mixed[-2])
print(mixed[-1][0])

# 30~11
print(numbers[2:5])
print(numbers[::-1])

### 리스트의 데이터 변경하기 (인덱싱을 통해 값 변경)
# 원본 데이터가 변경
numbers = [25, 27, 30, 32, 34, 36]
numbers[2] = 100
print(numbers) # [25, 27, 100, 32, 34, 36]

### in, not in -> True, False 로 결과 확인 가능
machines = ["펌프", "모터", "압축기"]
print("펌프" in machines) # True
print("펌프 " in machines) # False
print("실린더" not in machines) # True

##### 실습 문제
temp = [30,50,70,80,88,99,100]
print(temp[0],temp[2],temp[-1])

##### 실습 문제
prod = [1,2,3,4,5,6]
part1, part2 = prod[0], prod[-1]
print(part1+part2)
print((part1+part2)/2)

##### 리스트 함수 사용해보기 ########
# 리스트.index(요소) -> 리스트 안에 요소가 몇번째로 등장하는지
# 요소가 없으면 Error
numbers = [25, 80, 30, 50, 11, 12]
# print(numbers.index(100)) # ValueError: 100 is not in list
print(numbers.index(50)) 


## 리스트.append(값) -> 리스트의 맨 뒤에 원하는 값 추기

## 리스트.insert(위치인덱스, 값) -> 리스트의 특정 위치인덱스에 원하는 값을 추가

## 리스트.extend(리스트2) -> 리스트1에 리스트2를 붙혀주는 함수
data = [25,26,27]
data.append(30)
print(data)

data.insert(0,24)
print(data)

data.extend([29,31,32])
print(data)

##### 실습 문제
list = []
list.append(30)
print(list)

list.insert(0,28)
print(list)

list.extend([31,32])
print(list)

list.insert(-1,50)
print(list)
list.insert(100,100)
print(list)
# 리스트끼리의 덧셈 연산 가능, 리스트 *숫자 연산(반복) 가능
print([1,2,3]+[4,5,6]) # [1, 2, 3, 4, 5, 6]
print([1,2,3]*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

### 리스트.remove(값)
### 리스트.pop(위치) 
# -> pop의 반환값이 존재해서 제거되는 값을 따로 저장 가능
# 번호를 쓰지 않으면 맨 뒤에서 데이터 제거
### del 리스트(인덱싱 or 슬라이딩)
data = [25,26,27,28,29,30]
value1 = data.remove(25)
print(data) # [26, 27, 28, 29, 30]
print(value1) # None

value2 = data.pop(2) # 67번 라인에서 제거됨 결과 이후 변수가 저장되기 때문
print(data) # [26, 27, 29, 30]
print(value2) # 28

del data[2] # 70라인 기준으로 인덱싱
print(data)
del data[1:] # [26,27,30]
print(data) # [26]

temps = [25,26,999,24,28,26]
temps.remove(999)
print(temps)

x = temps.pop(1)
print(x)
del temps[0]
print(temps)

### 리스트 탐색, 정렬
# 리스트.sort() -> 기본적으로 오름차순 정렬, 괄호 안에 reverse=True 옵션 작성시 내림차순 가능 
# 리스트.reverse() -> 리스트의 순서를 거꾸로 뒤집어줌. (원본 리스트 변경)
# 리스트.count(), 리스트.index()
data = [27, 24, 30, 22, 26]
data.sort()
print(data) 

data.sort(reverse=True)
print(data)

data = [27, 24, 30, 22, 26]
data.reverse()
print(data)

raw_data = ["정상", "이상", "이상", "정상", "이상"]
print(raw_data.count("정상")) # 2
print(raw_data.index("이상")) # 1


temp = [27, 24, 30, 22, 26, 24, 28]
temp.sort()
print(temp)

temp.reverse()
print(temp)

print(temp.count(24))
print(temp.index(24))