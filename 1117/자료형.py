# int 정수형
# float 실수형
# str 문자열
# bool 논리형

count = 3 # int
temp = 25.5 # float
name = "센서A" # str
empty = "" # str
ok = True # bool
no = False # bool
print(count > temp) # False
print(count < temp) # True

### type() 함수 사용해보기 - 자료형 확인
print(type(25)) # <class 'int'>
print(type("25")) # <class 'str'>
print(type(25>24)) # <class 'bool'>
print(type(25.0)) # <class 'float'>

### 문자열, 숫자형의 더하기 연산자 사용
print(80+70) # 150
print("80" + "70") # 8070
print(type(80+70)) # <class 'int'>
print(type("80" + "70")) # <class 'str'>

### 실수형의 더하기
print(0.1 + 0.2)
print(round(0.1 + 0.2, 2)) # 0.3

### 숫자와 문자열의 계산
a = 100
print(a + 10)
# print(a + "10") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(10/2) # 5.0, 나누기의 결과는 정수형이 아니라 실수형이다.


