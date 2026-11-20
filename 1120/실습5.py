num1 = input("숫자 5개 입력: ").split()
num2 = [int(num1[0]), int(num1[1]), int(num1[2]), int(num1[3]), int(num1[4])]
num2.sort()
print("정렬 결과: ",num2)
print("중앙값:" ,num2[2])