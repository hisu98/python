# +(문자열 이어주기) *(문자열 반복)
print("설비"+"점검") # 설비점검
print("설비"+''+"점검") # 설비점검
line = '='*20 #구분선 만들어주기
print(line)

##### 문자열과 관련된 함수
# len(문자열) : 문자열의 길이를 반환
print(len("PYTHON")) # 6
print(len("Strawberry Moon ~!")) # 18 
phone = '01012341234'
phonelength = len(phone)
print(phonelength)

# in, not in < 함수는 아님
hasWord = "고장" in "설비 고장을 예측하는 ~~"
hasWord2 = "고장" not in "설비 고장을 예측하는 ~~"
print(hasWord, hasWord2)

# 실습
msg = "설비 고장 발생"
print("고장" in msg)
print("정상" in msg)

# count(), find(), index()
# 문자열A.count("문자열B") : 문자열A에 문자열B가 몇 개나 들어있는지 -> 숫자값 반환
# 문자열A.find("문자열B") : 
# - 문자열A에 문자열B가 언제 처음 등장하는지 -> 인덱스 반환
# -문자열 B가 등장하지 않으면 -1
# 문자열A.index(문자열B) : 
# - 문자열 A가 문자열B가 언제 처음 등장하는지 -> 인덱스 반환
# - 문자열B가 등장하지 않으면 Error! 
print("banana".count("a")) # 3
print("banana".count("na")) # 2

email = 'hong@company.com'
print("@의 인덱스번호", email.find("@")) # 4
print("@의 인덱스번호", email.find("!")) # -1 -> 찾고자 하는 문자열이 없음

print("@의 인덱스번호", email.index("@")) # 4
# print("@의 인덱스번호", email.index("!")) # ValueError: substring not found

# 실습 문제3
text = "sensor-01-temp"
print(text.count("-"))   # 2 

# 실습 문제4
text = "temp_2024"
print(text.find("_")) # 4
print(text.find("6")) # -1

# startswith / endswith
# 문자열A.startwith("문자열B") : 문자열A가 문자열B로 시작하는지 검사 -> T/F
# 문자열A.endswith("문자열B") : 문자열A가 문자열B로 끝나는지 검사 -> T/F
print("EQP-001".startswith("EQP")) # True 
print("data.csv".endswith(".csv")) # True
print(""=="") #False
print("normal" == "NORMAL") #False
print("AAaaBB" == "AAaaBB") #True


