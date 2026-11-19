# 변수 선언
# 변수_이름 = 할당할값
# 등호 표시가 같다는 의미가 아닌 대입의 의미
temp = 25
name = "센서A"
print(temp)
print(name)

x = 10
print("처음할당 된 후의",x)
x = 15
print("재할당된 후의",x)

x = x + 5 #직전의 x를 연산하여 다시 x에 대입
print("연산후의 x:", x)

## 변수이름 규칙
# 숫자로 시작되면 안됨, 특수문자는 언더바(_)만 허용이 됨
# 파이썬에서는 변수명 규칙을 snake_case 를 사용하도록 권장됨
# 변수명에는 공백이 있을 수 없음
sensor_count = 3 # snake_case, python 변수명 짓기 규칙
sensorCount = 3 # camelCase, 에러는 아니지만 권장되지 않습니다.
print(sensor_count, sensorCount)

temp2 =25
print(temp2)

# if = 15, # if, for, False 같은 예약어는 변수 이름으로 사용할 수 없음.

# 대소문자도 변수명에서 구분된다.
temp = 10
Temp = 100
print("temp, Temp", temp, Temp)

score = 50
score = 70
score = 90
print("score:", score)

## 다른 변수의 값 담기
a = 10
b = a
a = 11
print("a:", a)
print("b:", b)
# alt + shift + 방향키(위/아래) -> 한줄 복사

## 변수 선언 한줄에 여러개 하기
width, height = 4, 3
print("가로:", width)
print("세로:", height)
print("직사각형의 넓이:", width * height)

# x, y = 1, 2, 3 # valueError : too many values to unpack

# NameError
value = 15 # 먼저 정의가 되어있어야
print(value) # 


# 실습1
temp = 25
print(temp)
name = "센서A"
print(name)

# 실습2
temp = 30
print(temp)
temperature = 30
print(temperature)

# 실습3
my_number = 77
print(my_number)
mood = "오후"
print(mood)

# 실습4
age = 29
label = "나이" 
print(label)
print(age)