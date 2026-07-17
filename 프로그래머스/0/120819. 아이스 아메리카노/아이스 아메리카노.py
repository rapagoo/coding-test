def solution(money):
    answer = [0]*2
    cups = 0
    remaining = 0
    answer[1] = money
    while money>=5500:
        money -= 5500
        answer[0] += 1
        answer[1] -= 5500
    return answer