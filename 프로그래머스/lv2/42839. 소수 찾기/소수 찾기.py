# 순열 조합 import
from itertools import permutations

# 소수 찾는식
def sosu(x) :
    # 일단 소수라는 건 자기와 1 이라도 나와야 소수자격이되는데
    # 2보다 작으면 약수는 1밖에 없으니 탈락
    if x < 2 :
        return False
    
    # 자기 자신과 1말고 나누어 떨어지는 수 찾는 식
    # 만약에 있다면? 소수자격 탈락
    for i in range(2, x) :
        if x % i == 0 :
            return False
    
    # 다 통과한 숫자 합격
    return True

def solution(numbers):
    answer = 0
    nums = []
    
    
    # 순열 모듈 사용해서 나올 수 있는 모든 수
    for i in range(1, len(numbers)+1) :
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
    
    # 그걸 깔끔하게 가져와 
    sunyeol = list(set(map(int, set(sum(nums, [])))))
    
    for j in sunyeol :
        if sosu(j) == True :
            answer += 1

    return answer
# 숫자로 만들 수 있는 조합을 짜고 담은 다음
# 중복 제거하고 % 써서 나머지 0 인거 뽑고 len 2인거 return