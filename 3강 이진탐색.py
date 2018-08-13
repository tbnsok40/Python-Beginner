def solution(L, x):
	m_index = ((len(L))) // 2
	s_index = 0
	e_index = len(L) - 1

	while L[s_index] <= L[e_index] and ((L[s_index] or L[e_index]) != L[m_index]):
		if L[m_index] == x:
			return m_index

		elif L[m_index] < x:
			s_index = m_index
			m_index = (s_index + e_index) // 2

		else:
			e_index = m_index
			m_index = (s_index + e_index) // 2

	return -1

L = [2, 3, 5, 6, 9, 11, 15]

for x in L:
    sol = solution(L, x)
    print(sol)


	이진탐색 반복문

1. s_index 와 e_index의 범위를 정의 (s가 e보다 크지 않도록)
2. s_index 또는 e_index 어느 것도 m_index와 같아선 안된다. (그렇지 않으면 리스트 안에 찾고자 하는 수가 없기 때문.)
3. x 가 m_index 보다 클때 혹은 작을 때 마다 (1) s_index나 e_index를 조정해준 후 (2) m_index를 조정해줘야 한다.

	고칠 점
1. m_index = (0 + (len(L) - 1)) // 2 ==> 0 더할 필요 없고, -1 해줄 필요 없다.
2. ((L[s_index] or L[e_index]) != L[m_index]) ==> 파이썬에선
	L[s_index] == L[m_index] or L[e_index] == L[m_index] 처럼 표현해야 한다.
	또한 while 조건에서 이것을 검사하는 것은 이진탐색에서 권하고 싶은 방식이 아니다.

===========================응 다시해야해 ^^ ===========================================

def solution(L, x):
	m_index = ((len(L))) // 2
	s_index = 0
	e_index = len(L) - 1

	while s_index <= e_index:
            m_index = (s_index + e_index) // 2

            if L[m_index] == x:
                return m_index

            elif L[m_index] < x:
                s_index = m_index + 1

            else:
                e_index = m_index

	return -1

L = [2, 3, 5, 6, 9, 11, 15]
for x in L:
    sol = solution(L, x)
    print(sol)


1. 47번 줄에서 m_index를 한번만 선언해준다. 
2. 53번 줄에서 m_index뒤에 +1을 해주지 않아서 마지막 인덱스(15)에서 계속 오류가 났다.

