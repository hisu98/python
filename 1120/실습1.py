temp = 78
vib = 3.2
ele = 52
if temp > 80 or vib > 4.0:
    print("위험: 즉시 정지")
elif ele > 60 and temp > 70:
    print("주의: 부하 점검")
elif vib > 2.5:
    print("주의: 진동 관찰")
else:
    print("정상")