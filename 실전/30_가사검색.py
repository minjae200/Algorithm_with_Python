from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

def solution(words, queries):
    words_by_length = [[] for _ in range(10001)]
    r_words_by_length = [[] for _ in range(10001)]
    for word in words:
        words_by_length[len(word)].append(word)
        r_words_by_length[len(word)].append(word[::-1])
    for i in range(10001):
        words_by_length[i].sort()
        r_words_by_length[i].sort()
    answer = []
    for query in queries:
        if query[0] != '?':
            answer.append(count_by_range(words_by_length[len(query)], query.replace('?', 'a'), query.replace('?', 'z')))
        else:
            answer.append(count_by_range(r_words_by_length[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')))
    return answer

if __name__ == '__main__':
    words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']
    queries = ['fro??', '????o', 'fr???', 'fro???', 'pro?']
    print(solution(words, queries))