# 실습1
count = 7
temp = 9.9
name = "오후"
is_ok = True
print(count, temp, name, is_ok)

# 실습2
print(type(count))
print(type(temp))
print(type(name))
print(type(is_ok))

# 실습3
# 100 -> 정수(int)
# 100.0 -> 실수(float)
# "100" -> 문자열(str)
print(type(100))
print(type(100.0))
print(type("100"))

# 실습4
print(20+30)
print("2" + "3")
print("20" + "30")
# 숫자 20 + 30은 50이 되지만 글자 "20" + "30"은 나란히 붙어서 2030이 된다.

# 실습5
print(3 > 2)
print(5 == 5)
print(type(3 > 2))
print(type(5 == 5))

# 실습6
num = 77
print(type(num))
num = 77.0
print(type(num))
num = "77"
print(type(num))

#실습7
device_temp = 26.7  # 온도는 소수점 포함 실수 표현
check_count = 5 # 점검 횟수는 떨어지는 정수 표현
device_name = "설비7" # 설비 이름은 문자열 표현
is_normal = True # 정상 여부는 참, 거짓 여부인 bool으로 표현