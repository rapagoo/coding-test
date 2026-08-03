def solution(n):
    count = 1
    while True:
        if n % count == 1:
            return count
        else:
            count += 1