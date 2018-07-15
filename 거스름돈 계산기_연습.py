def calculate_change(payment, cost):
    dif = payment - cost

    print("50000원 지폐: %d장" %(dif // 50000))
    dif2 = dif - 50000*(dif//50000)
    print("10000원 지폐: %d장" %(dif2//10000))
    dif3 = dif2 - 10000*(dif2//10000)
    print("5000원 지폐: %d장" %(dif3//5000))
    dif4 = dif3 - 5000*(dif3//5000)
    print("1000원 지폐: %d장" %(dif4//1000))

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
