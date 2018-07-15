
i = 4
from random import randint
y = randint(1,20)

while i >= 1:

    x = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " %i))

    if x > y:
        print("Down")
    elif x < y:
        print("Up")
    else:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." %(5 - i))
        break
    i = i - 1
if i == 0:
    print("아쉬웠습니다. 정답은 %d였습니다." %y)
