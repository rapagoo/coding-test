def solution(n):
    array = list(str(n))
    array.reverse()
    answer = []
    for i in array:
        answer.append(int(i))
    return answer