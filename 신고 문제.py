sample_id_list = ["muzi", "frodo", "apeach", "neo"]
sample_report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report_list = {}
    reported_number = {}
    banned = []

    for id in id_list:
        report_list[id] = []

    for rp in report:
        if rp.split(' ')[1] in report_list[rp.split(' ')[0]]:
            pass
        else:
            report_list[rp.split(' ')[0]].append(rp.split(' ')[1])

    for values in report_list.values():
        for value in values:
            if value not in reported_number:
                reported_number[value] = 1

            else:
                reported_number[value] += 1

    for r, v in reported_number.items():
        if v >= k:
            banned.append(r)

    tmp = 0
    for values in report_list.values():
        if values:
            for value in values:
                if value in banned:
                    answer[tmp] += 1
                else:
                    pass
            tmp += 1

        else:
            tmp += 1

    return answer

print(solution(sample_id_list, sample_report, 2))



