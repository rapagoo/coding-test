def solution(hp):
    first_ant = hp // 5
    second_ant = (hp % 5) // 3
    third_ant = hp % 5 % 3
    return first_ant+second_ant+third_ant