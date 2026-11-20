num1 = float(input("첫 번째 숫자: "))
num2 = float(input("두 번째 숫자: "))
op = input("연산자 (+, -, *, /): ")

match op:
    case "+":
        print("계산 결과:", num1 + num2)
    case "-":
        print("계산 결과", num1 - num2)
    case "*":
        print("계산 결과", num1 * num2)
    case "/":
        print("계산 결과", num1 / num2)
    case _:
        print("오류: 지원하지 않는 연산자입니다")