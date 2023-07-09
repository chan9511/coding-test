from itertools import permutations

def is_prime_number(x) :
    if x < 2 :
        return False
    
    for i in range(2, x) :
        if x % i == 0 :
            return False
            
    return True

def solution(numbers):
    answer = 0
    nums = []
    
    for i in range(1, len(numbers)+1) :
        #순열 모듈 사용해서 나올 수 있는 모든 수 조합
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
    per = list(set(map(int, set(sum(nums, [])))))
    
    for p in per :
        if is_prime_number(p) == True :
            answer += 1

    return answer
# 숫자로 만들 수 있는 조합을 짜고 담은 다음
# 중복 제거하고 % 써서 나머지 0 인거 뽑고 len 2인거 return