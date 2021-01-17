def solution(N, stages):
    answer = []
    people = len(stages)

    for i in range(1, N+1):
        stage_user = stages.count(i)
        fail = (stage_user / people) if people != 0 else 0
        answer.append((i,fail))
        people -= stage_user

    answer.sort(key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer

# if __name__ == '__main__':
#     print(solution(5,[2,1,2,6,2,4,3,3]))