sample_lotto = [44, 1, 0, 0, 31, 25]
sample_lotto_win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    answer = [0, 0]
    lottos_num = len(lottos)
    lottos.sort()
    win_nums.sort()
    removed = 0

    for win_num in win_nums:
        if win_num in lottos:a
            lottos.remove(win_num)
            removed += 1
        else:
            pass

    answer[0] = 7 - lottos.count(0) - removed if 7 - lottos.count(0) - removed <= 5 else 6
    answer[1] = 1 + lottos.count(0) + (lottos_num - removed) if (lottos_num - removed) + lottos.count(0) <= 5 else 6
    return answer

print(solution(sample_lotto, sample_lotto_win_nums))

