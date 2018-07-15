year = 2016
month = 1
day = 16
day_of_week = "일"

print("오늘은" + str(year) + "년" + str(month) + "월" + str(day) + "일" + day_of_week + "요일입니다.")

print("오늘은 %d년 %d월 %d일 %s입니다." %(year, month, day, day_of_week))
print("오늘은 %d년 %d월 %d일 %s입니다." %(year, month + 1, day + 1, day_of_week))

print(1.0 / 3)
print("1 나눈기 3은 %f" %(1.0 / 3))
print("1 나눈기 3은 %.4f" %(1.0 / 3))
print("1 나눈기 3은 %.2f" %(1.0 / 3))