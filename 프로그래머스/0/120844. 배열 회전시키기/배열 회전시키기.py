def solution(numbers, direction):

    if direction == "right":
        for i in range(len(numbers)-1, 0, -1):
            numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
    else:
        for i in range(len(numbers)-1):
            numbers[i+1], numbers[i] = numbers[i], numbers[i+1]
    return numbers