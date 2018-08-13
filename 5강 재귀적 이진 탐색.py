def solution(L, x, l, u):
    if l >= u:
        return -1

    mid = (l + u) // 2

    if x == L[mid]:
        return mid

    elif x < L[mid]:
        return solution(L, x, l, mid)

    else:
        return solution(L, x, mid + 1, u)

    고칠 점
1. 14번 줄: mid + 1 빼먹지 않기
2. 2번줄: if x not in L ==> O(n)가 되므로 리스트 길이에 따라 무한정 길어진다.
   간단히 생각해서, 이진 반복문에선 처음 인덱스가 마지막 인덱스 보다 크면 타깃 값이 없는걸로 간주한다.
   이 점을 활용.
