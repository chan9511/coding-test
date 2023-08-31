# 조합을 설정했으면 중복(x)
# 각 종류별로 1가지 의상만 착용가능.
# 카테고리가 중복되지 않는 경우의 수 return

def solution(clothes):
    # closet = 착장(?) 을 넣기 위한 빈 dict 생성
    closet = {}
    answer = 1
    for element in clothes:
        # key = 카테고리
        key = element[1]
        # value = 카테고리안에 제품명
        value = element[0]
        
        # 착장에 key(카테고리)가 담겨있다면 key의 value값을 착장에 추가
        # 
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]
            
     # ex) output: {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}
     # 위와 같이 딕셔너리가 만들어진다.
    
    for key in closet.keys():
        answer = answer * (len(closet[key]) + 1)
    return answer - 1

# 질문 1 