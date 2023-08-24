def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    # AXB * BXC => AXC
    # arr1 [[1, 4], [3, 2], [4, 1]] => *3X2
    # arr2 [[3, 3], [3, 3]] => 2X2*
    
    for i in range(len(arr1)): # num row
        for j in range(len(arr2[0])): # num col
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer