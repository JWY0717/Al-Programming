import tsp
import random

LIMITS = 100

def first_choice(p):
    current = tsp.random_init(p)
    value_distance = tsp.evaluate(current,p)
    ## 알고리즘 활용해서 최적의 값을 변경하는 코드를 작성
    i = 0
    while i < LIMITS:
        succesor = random_mutant(current,p)
        _value_distance = tsp.evaluate(succesor, p)
        if _value_distance < value_distance:
            current = succesor
            value_distance = _value_distance
            i = 0
        else:
            i = i + 1
    return current, value_distance


# 해당 변이를 주는 것이 말이 안됨
def random_mutant(current, p):
    while True:
        # 일단 해당 좌표를 받아옴 
        i , j = sorted([random.randrange(p[0]) for _ in range(2)])
        if i < j:
            cur_copy = inversion(current,i,j)
            break
    return cur_copy


def inversion (current, i, j):
    cur_copy = current[:]
    while i < j:
        # i와 j의 위치교환
        cur_copy[i], cur_copy[j] = cur_copy[j], cur_copy[i]
        i = i + 1
        j = j - 1 
    return cur_copy

if __name__ == " __main__":
    p = tsp.create_problem("./data/tsp30.txt")
    solution, minimum = first_choice(p)
    print(solution)
    print(minimum)