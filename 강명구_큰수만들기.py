sample_number1 = '1924'
sample_number2 = '1231234'
sample_number3 = '4177252841'

def solution(number, k):
    nums = []
    for i in number:
        nums.append(int(i))

    cnt = len(number) - k - 1  # 남기는 숫자
    answer = []

    while True:
        if cnt == 0:
            break
        max_num = max(nums[:-cnt])  # k - 1 개 만큼 수를 남겨두고 나머지 안에서 최대 값을 answer 에 추가
        answer.append(str(max_num))  # 문자열로
        del nums[0:nums.index(max_num) + 1]  # 해당 최대 값과 그 앞의 요소들은 nums 에서 제거
        cnt -= 1  # 남겨야 할 숫자의 개수 -1

    answer.append(str(max(nums)))
    answer = ''.join(answer)
    return answer

print(solution(sample_number1, 2))
print(solution(sample_number2, 3))
print(solution(sample_number3, 4))