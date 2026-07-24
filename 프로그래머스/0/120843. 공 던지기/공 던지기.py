def solution(numbers, k):
    result = numbers[0]
    idx = 0
    for i in range(k-1):
        idx += 2
        if idx >= len(numbers):
            idx -= len(numbers)
            
        result = numbers[idx]
        
    return result