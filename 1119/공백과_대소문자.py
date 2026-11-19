word = "python"
sentence = "I love python" 

# upper(), lower()
# capitalize(), title()
print(word.upper()) # PYTHON
print(sentence.upper()) # I LOVE PYTHON
print(word.count("p")) # 1 원본 문자열은 변경되지 않음

print("normal".upper())
print("WARNING".lower())
print("WARNING 경고".lower()) # warning 경고 (한글이나 특수문자는 그대로 유지)
print("python is good. i have an apple.".capitalize())
# Python is good. i have an apple.

print("python is good. i have an apple.".title())
# Python Is Good. I Have An Apple.
print("hong gil-dong".title()) # Hong Gil-Dong

print('apple'.lower() == "Apple".lower())

# isupper(), islower()
print("Apple".islower(), 'Apple'.isupper())
print('apple'.islower(),"APPLE".isupper())

# 실습
print("ready".upper())
print("WARNING".lower())
print("kim chul soo".title())
print("fault".upper() == 'FAULT'.upper())
print("ABC".isupper(),"ABC".islower())
print("abc".isupper(), "abc".islower())
print("Abc".isupper(), "Abc".islower())

word = "Sensor_Log.CSV"
word2 = print(word.lower())
print("sensor_log.csv".startswith("sensor"))
print("sensor_log.csv".endswith(".csv"))