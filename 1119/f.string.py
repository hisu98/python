name = "홍길동"
age = 25
# 홍길동님은 25살입니다.
sentence = name+'님은 '+ str(age)+ "살입니다" 
print(sentence)
sentence2 = f'{name}님은 {age}살입니다'
print(sentence2)

code = 'EQP-001'

print(f'설비 코드 {code} 점검 완료: 온도 {25}도')
hours = 3
print(f'총 가동 시간(분): {hours*60}분')

value = 3.141592
print(f"PI 소수점둘째자리까지: {value:.2f}")
print(f"PI 소수점둘째자리까지: {value:.4f}")



'''
# ① 설비명·온도를 변수로 저장 → ② f-string을 사용해서 예상 결과와 같이 출력

# ① 세 점수를 변수로 저장 → ② f-string을 사용하여 평균을 구하는 계산식을 사용해 출력

# ① 측정값 87.456 저장 → ② 소수점 첫 번째 자리와 두 번째 자리까지 각각 출력

# ① 문자열 '  5 , sensor_2 , WARNING , 0.78912  ' 저장
# ② strip·split 후 각 조각 정리, 소수점은 두 번째 자리까지

'''

# 1. 
name = 'seven'
temp = 25
print(f'설비명: {name}, 현재온도: {temp}도')

# 2.
score1, score2, score3 = 80, 90, 95
print(f'평균점수: {(score1+score2+score3)/3}점')

# 3.
score = 87.456
print(f'{score:.1f}')
print(f'{score:.2f}')

# 4.
data = ' 5 , sensor_2 , WARNING , 0.78912 '
parts = data.strip().split(' , ')
print(parts)

print(f'{parts[0]} {parts[1]} {parts[2]} {float(parts[3]):.2f}')