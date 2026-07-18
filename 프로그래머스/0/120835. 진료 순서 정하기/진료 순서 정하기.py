def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    answer=[]
    for i in range(len(emergency)):
        answer.append(sorted_emergency.index(emergency[i])+1) 
    return answer