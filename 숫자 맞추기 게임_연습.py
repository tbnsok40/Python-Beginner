from random import randint
x = randint(1,20)
for i in range(1,5):
    if i < 5:
        y = int(input("기회는 %d 번 남았습니다.:" %(5 - i)))

        if x > y:
            print("UP")
        elif x < y:
            print("DOWN")
        else:
            print("CORRECT %d번만에 맞췄습니다." %(5 - i))
            break

if x > y or x < y:
    print("정답은 %d였습니다." %(x))
