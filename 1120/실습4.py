money1 = int(input("현재 잔액: "))
money2 = int(input("출금 금액: "))
if money2 % 1000 != 0:
    print("실패 : 출금액은 1,000원 단위여야 합니다")
elif money2 < 1000 or money2 > 100000:
    print("실패 : 출금액은 1,000~100000원이여야 합니다")
elif money2 > money1:
    print("실패: 잔액이 부족합니다")
else:
    print("출금 성공")
    print(f'남은 잔액 : {money1-money2}원')