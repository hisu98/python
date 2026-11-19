## 산술 연산자
# + - * /
# //(몫) %(나머지) **(거듭제곱)

print(3 + 5)
print(3 - 5)
print(3 * 5)
print(10 / 4)

print(11 // 3) # 3
print(11 % 3) # 2
# 5는 홀수 -> 2로 나눴을 때 나머지가 1이면 홀수

print(10 ** 5)

### 연산자의 우선순위
# ** > * > / > // > % > +,-
print(2 + 5 * 3) # 17
print((2 + 5) * 3) # 21

#### 문자열 연산
print("*"*20)
print("안녕"+"하세요"+"!!!")

#### 복합 할당 연산제
score = 70
score = score + 30 # 100
score += 30 # score = score + 30
print("score", score)  # 130

score = 70
score = score - 30 # 40
score -= 30 # 10
print("score", score) # 10

#============비교, 논리 연산자===========
# ==(같다) !=(다르다) > < >= <=
# and or not
number1 = 3
number2 = 5
print(number1 < number2) # True
print(number1 > number2) # False
print(number1 <= number2) # True
print(number1 >= number2) # False
print(number1 == number2) # False
print(number1 != number2) # True

print("=================")
print(True and True and True and False) # False
print(True or True or True or False) # True
print(not(True or True or True or False)) # False
print((True and True) and (True or False)) # True

temp = 80
print(temp > 80 and temp < 100) # False
print(not(temp>90)) # True



