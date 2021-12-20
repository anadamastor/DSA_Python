# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(T):
    # write your code in Python 3.6
    hours = T // 3600
    min = (T % 3600) // 60
    sec = T - (min * 60 + hours * 3600)
    return (f"{hours}h{min}m{sec}s")

print(solution(7200))