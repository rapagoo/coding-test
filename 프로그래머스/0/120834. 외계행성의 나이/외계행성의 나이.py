def solution(age):
    text = str(age)
    answer=''
    for c in text:
        answer += chr(int(c)+97)
    return answer