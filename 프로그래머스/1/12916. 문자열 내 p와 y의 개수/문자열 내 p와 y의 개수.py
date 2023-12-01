# p의 개수와 y의 개수가 같다면 True 를 반환, 아니면 False 반환하는 문제
# s의 p의 개수를 알 수 있는 방법 -> s.count('p')
# 1번 풀이 (채점 60점)
#def solution(s):
#    if s.count('p') == s.count('y'):
#        return True
#    else:
#        return False
# 2번 풀이 (채점 60점)
#def solution(s):
#    if s.count('p') == s.count('y'):
#        return True
#    elif s.count('p') != s.count('y'):
#        return False
#    elif s.count('p') == s.count('y') == 0:
#        return False
# 3번 풀이
# 대문자 소문자를 구별하지 않는 걸 확인을 못해서 다시 시도
# 주어진 문자열을 소문자로 바꿔서 개수 확인
def solution(s):
    if s.lower().count('p') == s.lower().count('y'):
        return True
    else:
        return False