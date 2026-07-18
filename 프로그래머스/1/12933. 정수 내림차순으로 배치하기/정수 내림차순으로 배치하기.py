def solution(n):
    num_list = sorted(list(str(n)), reverse=True)
    num = int(''.join(num_list))
    return num
    