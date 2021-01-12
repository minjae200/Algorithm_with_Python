# https://programmers.co.kr/learn/courses/30/lessons/60058


def get_balanced_index(w):
    count = 0
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        elif w[i] == ')':
            count -= 1
        if count == 0:
            return i
        
def is_correct_string(w):
    count = 0
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        elif w[i] == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

def solution(p):
    if p == '':
        return ''
    balanced_index = get_balanced_index(p)
    u = p[:balanced_index+1]
    v = p[balanced_index+1:]
    if is_correct_string(u):
        return u + solution(v)
    temp = ''.join(list(map(lambda x: '(' if x == ')' else ')', u[1:-1])))
    return '(' + solution(v) + ')' + temp

if __name__ == '__main__':
    a = ')('
    b = '(()())()'
    c = '()))((()'
    print(solution(a))
    print(solution(b))
    print(solution(c))