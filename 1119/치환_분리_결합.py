# replace -> 문자열 바꾸기, 지우기
print(" 정 상 가 동".replace(" ", "-")) # 공백제거
print(" 정 상 가 동".replace(" ", ""))  # 고장

#"3,000" -> 숫자 3000
print(int("3,000".replace(",", ""))) # int형 3000
#010-1234 5678 -> 0102345678
print("010-1234 5678".replace("-","").replace(" ", "")) # 01012345678

# 문자열.split(생략가능구분자)
list = [10, 20, 30, "hello", False]
print(list[3]) # hello
print(list[1]) # 20

coffee = "에스프레소 카페라떼 아메리카노"
print(coffee.split()) # ['에스프레소', '카페라떼', '아메리카노']
coffee_list = coffee.split()
print(coffee_list[2]) # 아메리카노

print("사과,배,감".split(",")) # ['사과', '배', '감']
print("사과,배,감".split(",")[2]) # 감
date = "2025-01-15"
day = date.split("-")
print(day[2])

print(coffee.split(" ", 1))


'''
#① '설비 정상 가동' 저장 → ② '정상'을 '점검'으로 바꿔 출력
#① 'PUMP A 03' 저장 → ② 공백 기준 분리하여 리스트 출력
#① 'a,b,c,d' 저장 → ② ','을 기준으로 분리
#① 'a,b,c,d' 저장 → ② 첫 번째 ','을 기준으로 한 번만 나누기
'''
text1 = "설비 정상 가동"
print(text1.replace("정상", "점검"))

text2 = "PUMP A 03"
print(text2.split())

text3= "a,b,c,d"
print(text3.split(","))
print(text3.split(",", 1))

# 구분자가 될 문자열.join([리스트])
list1 = ['2026', '11', '19']
# 2026-11-19, 2026.11.19
print('-'.join(list1))
print('.'.join(list1))

'''
#1. ① ['2025','01','15'] 준비 → ② '-'으로 연결하여 합치기

#2. 2025·1·15 를 '-' 와 ','로 총 2가지 방법을 사용해 이어서 출력

# 3. ① '2025/01/15' 저장 → ② '/'을 기준으로 나눈 후 '-' 으로 합치기

#4. ① '1, NORMAL ,25.3' 저장
② ',' 기준으로 나누어 1번 인덱스를 공백 제거와 소문자로 변환해 출력
'''

list = ['2025', '01', '15']
print('-'.join(list))
print(','.join(list))

prac2 = '2025·1·15'
print(prac2.replace('·','-'))
print(','.join(prac2.split('·')))

date = "2025/01/15"
print('-'.join(date.split("/")))

prac4 = '1, NORMAL, 25.3'
prac4 = prac4.split(',')
print(prac4[1].strip().lower())


'''
1. text = "   PyThOn   " ->"python"

2. phone = "  010 - 1234 - 5678  " -> "01012345678"

3. name = "   kIM    cHUL   sOO   " -> "Kim Chul Soo"

4. filename = "  Sensor Data 2026.CSV  " -> "sensor_data_2026.csv"

5. data = "TEMP----PRESSURE----STATUS" -> "TEMP-PRESSURE-STATUS"
'''

# 1.
text = " PhThOn "
print(text.strip().lower())
# 2.
phone = " 010 - 1234 - 5678 "
print(phone.replace(" ","").replace("-", ""))
print(phone.replace(" - ","").strip())
# 3.
name = " kIM   cHUL   sOO"
print(" ".join(name.split()).title())
# 4.
filename = " Sensor Data 2026.CSV"
print(filename.strip().lower().replace(" ","_"))
# 5.
data = "Temp----PRESSURE----STATUS"
print(data.replace("----", "-"))