# 인덱싱
word = 'PYTHON'
print(word[0],word[2], word[5])
print(word[-6],word[-4],word[-1])
print('python'[2])

word = "Strawberry Moon ~!"
print(word[0]+word[12]+word[14]+word[17])
word1 = "SIGNAL"
print(word1[0],word1[2],word1[5])
# print(word1[6]) # IndexError: string index out of range

word2 = "안녕하세요!"
greeting = word2[-6]+word2[-5]+word2[-1]
print(greeting)

# 슬라이싱
word = "PYTHON"
print(word[0:5]) # PYTHO
print(word[:4]) # PYTH
print(word[1:]) # YTHON
print(word[1:100]) # YTHON 최대한 가지고 올 수 있는 범위까지 실햄함
print(word[:]) # PYTHON

# 음수 인덱스를 통한 슬라이싱
#뒤에서부터 세글자
print(word[-3:])
# 마지막글자 빼고 가져와보기
print(word[:-1])

# 문자열[시작:끝:간격] - step 으로 건너뛰기
print(word[0::2]) # PTO
print(word[::-1]) # NOHTYP


# 실습
word3 = "SIGNAL"
print(word3[0:3])
print(word3[2:5])

# 실습2 "temp_sensor" 저장 -> 앞 4글자만 추가하기
practice = "temp_sensor"
print(practice[0:4])
# 실습3 "temp_sensor" 저장 -> _언더바 이후 모든글자 추출
print(practice[-6:])
# 실습4 'icecream' 저장 -> 슬라이싱만을 이용해서 crm 추출 
practice2 = "icecream"
print(practice2[1::3])