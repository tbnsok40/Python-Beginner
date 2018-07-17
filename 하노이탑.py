# def move_disk(disk_num, start_peg, end_peg):
#     print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))
#
# def hanoi(num_discs, start_peg, end_peg):
#     other_peg = 6 - start_peg - end_peg
#     if num_discs == 0:
#         return None
#     else:
#         hanoi(num_discs - 1, start_peg, 6 - start_peg - end_peg)
#         move_disk()
# # 테스트 코드 (포함하여 제출해주세요)
# hanoi(3, 1, 3)

# 구글답안
def hanoi(n, a, b, c):
    if n == 0: return
    hanoi(n - 1, a, c, b)
    print('%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동' %(n, a, c))
    hanoi(n - 1, b, a, c)
# n=int(input('enter: '))
hanoi(3, 1, 2, 3)


# 코드잇 답안
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_discs, start_peg = 1, end_peg = 3):
    if num_discs == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg
        hanoi(num_discs - 1, start_peg, other_peg)
        move_disk(num_discs, start_peg, end_peg)
        hanoi(num_discs - 1, other_peg, end_peg)

hanoi(3, 1, 3)