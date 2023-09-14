def solution(number, limit, power):
    answer = []
    ## 약수 먼저 구함
    for i in range(1,number+1):
        ## 약수 담을 곳
        yaksu = 0
        
        for j in range(1,int(i**(1/2))+1):
            if i % j == 0:
                yaksu += 1
                if j**2 != i:
                    yaksu += 1
            if yaksu > limit:
                yaksu = power
                break
        answer.append(yaksu)
    return sum(answer)