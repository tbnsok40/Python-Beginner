def calculate_change(payment, cost):
    dif = payment - cost

    a = ((dif) // 50000)
    print("50000원 지폐: %d장" %a)

    b = (dif - (a * 50000)) // 10000
    print("10000원 지폐: %d장" %b)

    c = (dif - (50000 * a + 10000 * b)) // 5000
    print("5000원 지폐: %d장" %c)

    d = (dif - (50000 * a + 10000 * b + 5000 * c)) // 1000
    print("1000원 지폐: %d장" %d)

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

