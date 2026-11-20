# 실습 1
data1 = " pump-07 | 08:30 | TEMP=085.5C | STATUS=normal "
data2 = "PUMP_07,09:00,92.0C,WARNING"
# 1번
parts1 = data1.strip().split(" | ")
parts2 = data2.strip().split(",")
# 2번
eq1 = parts1[0].upper().replace("-", "_")
eq2 = parts2[0].upper().replace("-", "_")
time1 = parts1[1]
time2 = parts2[1]
# 3번
temp1 = float(parts1[2].replace("TEMP=","").replace("C",""))
temp2 = float(parts2[2].replace("C",""))
#4번
status1 = parts1[3].replace("STATUS=","").lower()
status2 = parts2[3].lower()
# 5번
same_eq = (eq1 == eq2)
# 6번
temp_sub = (temp2-temp1)
increase_rate = (temp_sub/temp1) * 100
#7번
same_facility = same_eq and (temp_sub >= 6.0)
#8번
print("===== 센서 데이터 비교 =====")
print(f'설비코드: {eq1}')
print(f'최초측정: {time1} / {temp1}°C / {status1}')
print(f'최근측정: {time2} / {temp2}°C / {status2}')
print()
print(f'동일 설비 여부: {same_eq}')
print(f'온도 변화량: {temp_sub:.1f}°C')
print(f'온도 상승률: {increase_rate:.2f}%')
print(f'온도 급상승 여부: {same_facility}')