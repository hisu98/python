#1,2,3번
word = "NORMAL-WARNING-NORMAL-ERROR-WARNING" 
print(word.count("WARNING")) # 1번 2
print(word.count("NORMAL"))  # 2번 2
print(word.count("ERROR"))   # 3번 1

# 4번
first_index = word.find("WARNING") 
print("첫 번째 WARNING 시작 위치: ", first_index) # 4번 첫 번째 WARNING 시작 위치 : 7

# 5번
second_index = word.find("WARNING",first_index + 1) 
print("두 번째 WARNING 시작 위치: ", second_index) # 5번 두 번째 WARNING 시작 위치 : 28

# 6번
word2 = word[13:27] 
print(len(word2)) # 6번 14

# 7번
word3 = word[14:28]
print(word3) # 7번 -NORMAL-ERROR-

# 8번
print("ERROR" in word3) # 8번 True