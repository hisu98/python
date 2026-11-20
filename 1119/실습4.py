# 실습1
line1 = " LOT-A | 1,200 | 36 | 8h "
line2 = "lot_a,850,17,5h"

parts1 = line1.strip().split(" | ")
parts2 = line2.strip().split(",")
#1번
code1 = parts1[0].upper().replace("-","_")
code2 = parts2[0].upper()
#2번
prod1 = int(parts1[1].replace(",",""))
defect1 = int(parts1[2])

prod2 = int(parts2[1])
defect2 = int(parts2[2])
#3번
hours1 = int(parts1[3].replace("h",""))
hours2 = int(parts2[3].replace("h",""))
#4번
rate1 = (defect1 / prod1) * 100
rate2 = (defect2 / prod2) * 100
# 5번
improved = rate1 > rate2
#6번
total_prod = prod1 + prod2
total_defect = defect1 + defect2
# 7번
total_rate = (total_defect / total_prod) * 100
# 8번
total_hours = hours1 + hours2
avg_prod = total_prod / total_hours
# 9번
same_code = (code1 == code2)
final = same_code and improved
# 10번
print("====== 생산 데이터 분석 ======")
print(f"생산라인 코드: {code1}")
print(f"라인 코드 일치: {same_code}")
print()
print(f"[1차 생산] 생산량 {prod1}개 / 불량품 {defect1}개")
print(f"불량률: {rate1:.2f}%")
print(f"[2차 생산] 생산량 {prod2}개 / 불량품 {defect2}개")
print(f"불량률: {rate2:.2f}%")
print()
print(f"[통합 분석] 생산량 {total_prod}개 / 불량품 {total_defect}개")
print(f"통합 불량률: {total_rate:.2f}%")
print(f"시간당 평균 생산량: {avg_prod:.2f}개")
print()
print(f"불량률 개선 여부: {improved}")
print(f"최종 판정: {final}")