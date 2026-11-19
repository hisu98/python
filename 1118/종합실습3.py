'''
1. 인증 코드는 SEC-로 시작해야 합니다.
2. 인증 코드의 전체 길이는 15자여야 합니다.
3. 코드의 연도는 2026이어야 합니다.
4. 마지막 문자는 X 또는 Y 여야 합니다.
5. 세번째 항목의 네 자리 숫자는 1000 ~ 9999 사이여야 합니다.
6. 하이폰(-)이 정확히 3개 등장해야 합니다.
위의 모든 조건이 만족하는지 출력하세요. 
'''

user_code = input("인증 코드 형식을 입력해주세요: ")

# 1. 인증 코드는 SEC-로 시작해야 합니다.
code_start = user_code.startswith("SEC-")
print("1번 조건 만족?", code_start)
# 2. 인증 코드의 전체 길이는 15자여야 합니다.
user_code2 = len(user_code) == 15
print("2번 조건 만족?", user_code2)
# 3. 코드의 연도는 2026이어야 합니다.
user_code3 = user_code[4:8] == "2026"
print("3번 조건 만족?", user_code3)
# 4. 마지막 문자는 X 또는 Y 여야 합니다.
user_code4 = user_code[-1] == "X" or user_code[-1] == "Y"
print("4번 조건 만족?", user_code4)
# 5. 세번째 항목의 네 자리 숫자는 1000 ~ 9999 사이여야 합니다.
user_code5 = (int(user_code[9:13]) >= 1000 and
int(user_code[9:13]) <= 9999)
print("5번 조건 만족?", user_code5)
# 6. 하이폰(-)이 정확하게 3개 등장해야 한다.
user_code6 = user_code.count("-") == 3
print("6번 조건 만족?", user_code6)

isSignUp = (code_start and user_code2 and user_code3 and user_code4 and
user_code5 and user_code6)
print("최종 인증 결과:", isSignUp)



#인증 코드 형식을 입력해주세요: SEC-2026-5832-X
#1번 조건 만족? True
#2번 조건 만족? True
#3번 조건 만족? True
#4번 조건 만족? True
#5번 조건 만족? True
#6번 조건 만족? True
#최종 인증 결과: True

#인증 코드 형식을 입력해주세요: SEC-2026-0833-X
#1번 조건 만족? True
#2번 조건 만족? True
#3번 조건 만족? True
#4번 조건 만족? True
#5번 조건 만족? False
#6번 조건 만족? True
#최종 인증 결과: False