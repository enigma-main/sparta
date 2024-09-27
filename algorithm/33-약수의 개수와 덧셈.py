def solution(left, right):
    answer = 0
    
    sieve = [1] * 1001
    # fill sieve
    for i in range(2, right + 1):
        for j in range(1, 1000 // i + 1):
            sieve[i * j] += 1
    
    for i in range(left, right + 1):
        if sieve[i] % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer
