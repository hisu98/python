'''
0. 아이디, 비밀번호, 이메일을 받아서 계정 검증을 하는 프로그램.
1. 아이디 길이는 6자 이상 12자 이하입니다.
2. 아이디는 user_로 시작해야 합니다.
3. 비밀번호는 8자 이상이어야 합니다.
4. 비밀번호에는 ! 또는 @ 중 하나 이상이 포함되어야 합니다.
5. 비밀번호에 아이디 전체가 포함되어 있으면 안 됩니다.
6. 이메일은 @가 정확히 한 번 등장해야 합니다.
7. 이메일은 .com으로 끝나야 합니다.
모든 조건을 만족해야 최종 회원가입 가능 여부가 True가 됩니다.
'''

user_id = input("아이디를 입력해주세요: ")
password = input("비밀번호를 입력해주세요: ")
email = input("이메일을 입력해주세요: ")

### 아이디 조건
# 1. 아이디 길이는 6자 이상 12자 이하입니다. # and
id_length = len(user_id) >= 6 and len(user_id) <=12
print("1번 조건 만족?", id_length)
# 2. 아이디는 user_로 시작해야 합니다.
id_start = user_id.startswith("user_")
print("2번 조건 만족?", id_start)

#비밀번호 조건
# 3. 비밀번호는 8자 이상이어야 합니다.
pw_length = len(password) >=8
print("3번 조건 만족?", pw_length)
# 4. 비밀번호에는 ! 또는 @ 중 하나 이상이 포함되어야 합니다.
pw_word = ("!" in password) or ("@" in password)
print("4번 조건 만족?", pw_word)
# 5.비밀번호에 아이디 전체가 포함되어 있으면 안 됩니다.
pw_no_id = user_id not in password  # not(user_id in password)
print("5번 조건 만족?", pw_no_id)

# 이메일 조건
# 6. 이메일은 @가 정확히 한 번 등장해야 합니다.
email_at = email.count("@") == 1
print("6번 조건 만족?", email_at)
# 7. 이메일은 .com으로 끝나야 합니다.
email_end = email.endswith(".com")
print("7번 조건 만족?", email_end)
# 8. 모든 조건을 만족해야 최종 회원가입 가능 여부가 True가 됩니다.
isSignUp = (id_length and id_start and pw_length and pw_word and 
pw_no_id and email_at and email_end)
print("회원가입 가능?", isSignUp)