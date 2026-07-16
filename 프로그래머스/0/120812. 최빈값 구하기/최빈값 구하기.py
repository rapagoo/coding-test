def solution(array):
    count = [0] * 1001
    
    for n in array:
        count[n] += 1
    
    max_count = -1
    answer = -1
    for n in range(1001):
        if count[n] > max_count:
            max_count = count[n]
            answer = n
        elif count[n] == max_count:
            answer = -1
            
    return answer
            