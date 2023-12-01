# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 만들어야 한다.
# answer를 리스트 컴프리헨션을 사용해, x * i 값이 answer에 들어갈 수 있도록 만들어 주었다.
def solution(x,n):
    answer = [x * i for i in range(1,n+1)]
    return answer
