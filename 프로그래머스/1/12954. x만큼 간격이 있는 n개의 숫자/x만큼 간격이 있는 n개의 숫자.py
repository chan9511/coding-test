# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 만들어야 한다.
def solution(x,n):
    answer = [x * i for i in range(1,n+1)]
    return answer