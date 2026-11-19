# 실습 1
a, b = 17, 5
print(a+b) # 22
print(a-b) # 12
print(a*b) # 85
print(a/b) # 3.4
print(a//b) # 3
print(a**b) # 1419857

# 실습 2
a = int(input("첫 번째 숫자를 입력하세요(가로): "))  # 10
b = int(input("두 번째 숫자를 입력하세요(세로): ")) # 5
c = int(input("세 번째 숫자를 입력하세요(높이): ")) # 9

avg = (a+b+c) / 3 
area = (a**2)
volume = (a*b*c)
print("평균: ", avg) # 평균: 8.0
print("넓이: ", area) # 넓이: 100
print("부피: ", volume) # 부피: 450

# 실습 5
prod = 500
defect = 23
defect_rate = (defect/prod) * 100
print(defect_rate) # 4.6

# 실습 6
run_time = 21
total_time = 24
run_rate = (run_time/total_time) * 100
print(run_rate) # 87.5

# 실습 7
running_time = 98765
days = running_time // 86400
left1 = running_time % 86400

hours = left1 // 3600
left2 = left1 % 3600

minutes = left2 // 60
seconds = left2 // 60
print(days,"일",hours,"시간",minutes,"분",seconds,"초") # 1 일 3 시간 26 분 26 초

# 실습 8
temp = 85
press = 5
temp_good = temp >= 60 and temp <= 90
press_good = press >= 3 and press <= 7
all_good = temp_good and press_good
print("출력 결과: 온도 정상", temp_good, "압력정상", press_good, "모두정상", all_good)
# 출력 결과: 온도 정상 True 압력정상 True 모두정상 True
