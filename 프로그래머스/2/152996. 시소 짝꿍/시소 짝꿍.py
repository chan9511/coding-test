# 사람의 무게 * 거리 가 양쪽으로 서로 같다면 '시소 짝꿍' 이라함.
# 시소는 중심으로부터 2,3,4m 간격으로 좌석이 하나씩 있다.
# i 로 for문을 돌고 있을 때, 같은 수를 만나면 '시소 짝궁'으로 간주.
# weights를 순회하면서, 각 무게마다 무게*2, 무게*3, 무게*4 한 값끼리 모아준다
# 모인 사람들 끼리 중복 없이 조합을 짜면 된다고 생각했다.
# pair = {}

    # 무게에 대하여 모아주기
   # for i in range(len(weights)):
   #     w2, w3, w4 = weights[i] * 2, weights[i] * 3, weights[i] * 4
   #     pair.setdefault(w2, tuple())
   #     pair.setdefault(w3, tuple())
   #     pair.setdefault(w4, tuple())

   #     pair[w2] += (i,)
   #     pair[w3] += (i,)
   #     pair[w4] += (i,)
# 시간초과
from collections import Counter

def solution(weights):
    answer = 0
    
    # 1:1
    counter = Counter(weights)
    for k,v in counter.items():
        if v>=2:
            answer+= v*(v-1)//2
    weights = set(weights) 
    
    # 2:3 2:4 3:4 비율 가지면 짝궁 가능함
    for w in weights:
        if w*2/3 in weights:
            answer+= counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            answer+= counter[w*3/4] * counter[w]
    return answer
