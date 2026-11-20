# 실습1
log = " 2026/11/19 23:58:45 | DELAY=135s | EQP-09 "
# 1번
parts = log.strip().split(" | ")
date_time = parts[0].split()
date = date_time[0]
work_time = date_time[1]
time_delay = parts[1]
eq = parts[2]
# 2번
time_parts = work_time.split(":")
time_h = int(time_parts[0])
time_m = int(time_parts[1])
time_s = int(time_parts[2])
# 3번
delay_second = int(time_delay.replace("DELAY=","").replace("s",""))
# 4번
time_start = f'{time_h}시 {time_m}분 {time_s}초'
# 5번
time_total = (time_h*3600) + (time_m*60) + time_s
time_end = time_total + delay_second
day_second = 24 * 3600
next_day = time_end >= day_second
# 6번
remain_second = time_end % day_second
end_h = remain_second // 3600
end_m = (remain_second % 3600) // 60
end_s = remain_second % 60
# 7번, 8번
print("====== 설비 작업 정보 ======")
print(f'설비 코드: {eq}')
print(f'작업 날짜: {date}')
print(f'작업 시작 시간: {work_time}')
print(f'소요시간: {delay_second}')
print()
print(f'완료 시각: {end_h}시 {end_m}분 {end_s}초')
print(f'날짜 변경 여부: {next_day}')

