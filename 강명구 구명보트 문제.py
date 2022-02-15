sample_people = [70, 50, 80, 50]

def solution(people, limit):
    people.sort(reverse=True)  # 사람들을 몸무게의 역순으로 정렬
    boat = []
    tmp = 0
    while sum(people) != len(people) * 250:  # people 안의 모든 값이 250으로 바뀌면 반복문 종료
        boat.append([])  # 보트 하나 추가
        index = 0
        for person in people:
            if len(boat[tmp]) > 2:  # 보트 안에 두 명 이상 못 탐
                break

            if sum(boat[tmp]) + person <= limit:  # 보트 안 사람과 새로 탈 사람의 무게의 합이 limit 보다 적으면 탑승
                boat[tmp].append(person)  # tmp 번째 보트에 사람 탑승
                people[index] = 250  # 값을 250으로 바꿈 (몸무게 최대 값이 250 이므로)
            index += 1
        tmp += 1

    answer = len(boat)
    return answer

print(solution(sample_people, 100))

