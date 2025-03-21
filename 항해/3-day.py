# 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0

    start = 1
    end = max(times) * n

    while start <= end:
        mid = (start + end) // 2
        people = 0

        for time in times:
            people += mid // time
            if people > n:
                break
        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

print(solution(6, [7,10]))