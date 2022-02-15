def solution(prices):
    answer = []
    day = 1
    while True:
        if day == len(prices):
            answer.append(0)
            break

        nodown = [a for a in prices[-(len(prices) - day):] if a >= prices[day - 1]]
        answer.append(len(nodown))
        day += 1
    return answer


sample_price = [1, 2, 3, 2, 3]
print(solution(sample_price))