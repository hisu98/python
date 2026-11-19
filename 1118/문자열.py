name = '홍길동'
status = "정상"
code = 'EQP-001'
print(name, status, code)

sentence = "It's normal" # 바깥은 큰 따옴표로 작은 따옴표가 이미 나왔기 때문에
sentence2 = '이 장비는 "정상입니다."' # 여기는 반대로 큰 따옴표가 나와서 바깥쪽을 작은 따옴표로 감싼다.
print(sentence)
print(sentence2)

sentence3 = "'장비1'은 \"정상\"이고, '장비2'는 \"비정상\"입니다."
sentence4 = '\'장비1\'은 "정상"이고, \'장비2\'는 "비정상"입니다.'
print(sentence3)
print(sentence4)

#test = "여러줄로
#작성하면
#에러가 납니다.

삼중_따옴표 = '''여러줄로
작성했을 때
에러가 나지 않습니다.!!'''
print(삼중_따옴표)

##### 이스케이프 문자 \n \t \\
guide = "설비점검 하는 방법 \n 1. 전원 켜기 \n 2. 센서 확인"
print(guide)

print("이름\t상태")
print("설비1\t정상")

print("C:\\Users\\p3842\\Desktop\\데이터분석5기 수업자료")
print("\\") #\

print('2025', '01', '15', sep='-')

# 실습문제1
print("가동 점검표 \n1. 온도 확인, \n2. 압력확인")
print('''가동 점검표
1. 온도 확인
2. 압력확인''')

# 실습문제 2
code = "PUMP_A"
status = "정상"
date = "2025-01-15"
print(code + "/" + status + "/" + date)
print(code, status, date, sep="/")
print("처리중", end="...") # end는 맨 끝에 붙히는 용도