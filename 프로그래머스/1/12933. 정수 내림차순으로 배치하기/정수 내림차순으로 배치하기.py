def solution(n):
    num_list = sorted(list(str(n)), reverse=True)
    return int(''.join(num_list))