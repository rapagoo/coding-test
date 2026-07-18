def solution(n):
    text = str(n)
    ans = 0
    for c in text:
        ans += int(c)
    return ans