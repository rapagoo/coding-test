def solution(n):
    txt = str(n)
    answer = 0
    for c in txt:
        answer += int(c)
    return answer