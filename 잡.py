def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        release = 0
        while progresses:
            if progresses[0] >= 100:
                del progresses[0]
                release += 1
            else:
                break

        if release != 0:
            answer.append(release)

    return answer

sample_progresses1 = [93, 30, 55]
sample_progresses2 = [95, 90, 99, 99, 80, 99]
sample_speed1 = [1, 30, 5]
sample_speed2 = [1, 1, 1, 1, 1, 1]

print(solution(sample_progresses1, sample_speed1))
print(solution(sample_progresses2, sample_speed2))