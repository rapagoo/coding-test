def solution(s):
    numbers = s.split()
    int_numbers = []

    for number in numbers:
        int_numbers.append(int(number))
    min_value = min(int_numbers)
    max_value = max(int_numbers)
    
    return f"{min_value} {max_value}"