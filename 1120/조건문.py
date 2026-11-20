# score = int(input("점수를 입력해주세요(자연수로)"))
# if score >= 60:
    #print("합격입니다")
#else:
    #print("불합격입니다!")
#print("조건문과 관련없이 실행되는 문장입니다.")

# age = int(input("나이를 입력해주세요(자연수로)"))
# if age >= 20:
    # print("성인입니다")
#else:
    #print("미성년자입니다")

#score = int(input("점수릉 입력해주세요(자연수로)"))
# 90점 이상일 때 우수
# 70점 이상일 때 보통
# 그 아래일 때 미흡
#if score >= 90:
    #print("우수")
#elif score >= 70:
#    print("보통")
#else:
#    print("미흡")

#90점 이상일 때 A
#80점 이상일 때 B
#70점 이상일 때 C
#60점 이상일 때 D
#그 아래일 때 F

#score = int(input("점수를 입력해주세요(자연수로)"))
#if score >= 90:
#    print("A")
#elif score >= 80:
#    print("B")
#elif score >= 70:
#    print("C")
#elif score >= 60:
#    print("D")
#else:
#    print("F")

temp = 78
vib = 3.5
# 온도가 60초과 진동이 3 초고라면 위험합니다.
# 온도가 60초과 진동이 3 이하라면 주의하세요.
# 온도가 60 이하라면 정상입니다
if temp > 60:
    if vib > 3:
        print("위험합니다")
    else:
        print("주의하세요")
else:
    print("정상입니다")


# ===================================
#### 삼항 연산자
# 짝수인지 홀수인지 판단하는 프로그램
result1=""
number = 5
if number % 2 == 0:
    result1 = "짝수"
else:
    result1 = "홀수"
print(result1)

# 참일때값 if 조건 else 거짓일때값
result2 = "짝수" if number % 2 == 0 else "홀수"
# print("짝수") if number % 2 == 0 else print("홀수")
print(result2)

#### match ~ case 문
color = input("red, yellow, green 중 하나를 작성해주세요").strip()
# red -> 퇴장입니다
# yellow -> 경고입니다.
# green -> 통과입니다.
# 위 세개에 해당하지 않는다면 -> 잘못된 값이 들어왔습니다.
match color:
    case "red" | "RED":
        print("퇴장입니다")
    case "yellow":
        print("경고입니다")
    case "green":
        print("통과입니다")
    case _:
        print("잘못된 값이 들어왔습니다")

'''
match 변수:
    case 변수값1:
        변수 == 변수값1일 때 실행할 문장
    case 변수값2:
        변수 == 변수값2일 때 실행할 문장
    case 변수값3:
        변수 == 변수값3일 때 실행할 문장
    case _:
        변수가 변수값1, 변수값2, 변수값3 모두 아닐때 실행할 문장
        if-else문에서 else에 해당하는 문장
'''

# 설비코드, 온도, 상태
#data = ["PUMP-01", 85, "WARNING"]
# {설비명} : 온도{}도, 주의상태입니다.

#match data:
#    case [name, temp, "WARNING"]:
#        print(f'{name}: 온도 {temp}도, 주의상태입니다.')
#    case [name, temp, "WARNING"]:
#            print(f'{name}: 온도 {temp}도, 정상상태입니다.')

id = "admin"
pw = 1234
user_id = input("아이디를 입력해주세요")
user_pw = int(input("비밀번호를 입력해주세요"))
if user_id == id and user_pw == pw:
    print("로그인 성공")
else:
    print("로그인 실패")

