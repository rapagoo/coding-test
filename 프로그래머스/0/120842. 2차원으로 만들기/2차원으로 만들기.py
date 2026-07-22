def solution(num_list, n):
    answer = []
    temp_arr = []
    for i in num_list:
        temp_arr.append(i)
        if len(temp_arr) is n:
            answer.append(temp_arr)
            temp_arr=[]
    return answer