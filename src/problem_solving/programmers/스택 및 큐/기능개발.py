def solution(progresses, speeds):
    answer = []
    task = 0
    while sum(answer) < len(progresses):
        cnt = 0
        for i in range(task, len(progresses)):
            # 오늘 작업 진행
            progresses[i] += speeds[i]

        for i in range(task, len(progresses)):
            # 배포 가능한 작업은 배포
            if progresses[i] >= 100:
                cnt += 1
            else:
                task = i
                break

        if cnt != 0:
            answer.append(cnt)

    return answer


progresses = [[93, 30, 55], [95, 90, 99, 99, 80, 99]]
speeds = [[1, 30, 5], [1, 1, 1, 1, 1, 1]]
answers = [[2, 1], [1, 3, 2]]

for i in range(0, len(progresses)):
    my = solution(progresses[i], speeds[i])
    if my != answers[i]:
        print('틀림', my, answers[i])
    else:
        print('정답')
