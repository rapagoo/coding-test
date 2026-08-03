def solution(s):
    return True if s.count('P') + s.count('p') == s.count('y') + s.count('Y') else False