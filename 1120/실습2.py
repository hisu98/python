num1 = input("숫자 5개 입력: ").split()
num2 = [int(num1[0]), int(num1[1]), int(num1[2]), int(num1[3]), int(num1[4])]
num2.sort(reverse=True)
max_count = num2.count(num2[0])
print("두 번째로 큰 숫자: ", num2[max_count])