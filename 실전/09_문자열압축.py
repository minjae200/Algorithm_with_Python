#https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        current_string = s[:step]
        count = 1
        compression = ""
        for j in range(step, len(s), step):
            next_string = s[j:j+step]
            if current_string == next_string:
                count += 1
            else:
                compression += str(count) + current_string if count >= 2 else current_string
                current_string = next_string
                count = 1
        compression += str(count) + current_string if count >= 2 else current_string
        answer = min(answer, len(compression))
    return answer