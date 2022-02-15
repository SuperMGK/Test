def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        release = 0
        while progresses:
            if progresses[0] >= 100:
                del progresses[0]
                del speeds[0]
                release += 1
            else:
                break

        if release != 0:
            answer.append(release)

    return answer
