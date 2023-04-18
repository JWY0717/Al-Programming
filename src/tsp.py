import random
import math

# TODO: 인접행렬 그래프를 만들고 다시!
def create_problem(filename):
    f = open(filename, "r")
    # int 값 받아오기 조심!!!
    num_cities = int(f.readline())
    
    location = []
    
    for line in f.readline():
    # 좌표는 무조건 튜플(x,y)
        location.append(eval(line))
    f.close
    table = create_distance_table(num_cities,location)
    return num_cities,location, table

# 그래프 표현 == 행렬 == 2차원행렬 == 인접행렬 
# 인접행렬을 만들어야함1
# 좌표와 갯수가 필요!

def create_distance_table(num_cities,location):

    # 1. 거리를 계산해야 하는디1..
    #   - 유클리드 거리...
    #   - 점 두 개가 필요?
    table = []
    for i in range(num_cities):
        line = []
        for k in range(num_cities):
            distance = math.sqrt(((location[i][0]  - location[k][0]) **2) + (location[i][1]  - location[k][1]) **2)
            line.append(distance)
        table.append(line)
    return table



def random_init(p):
    # 결과 shuffle!!!
    n = p[0]
    init = list(range(n))
    # init은 값이 반환되어서 나감
    random.shuffle(init)
    return init
    


def evaluate(current, p):
    cost = 0
    num_cities,location, table = p
    # index를 써야 함으로 => num_cities
    for i in range(num_cities):
        cost = cost + table[current[i]][current[i-1]]
        
    return cost 



def describe_problem(p):
    print()
    n = p[0]
    print(f"Number of citeis : {n}")
    locations = p[1]
    for i in range(n):
        print(f"{locations[i]}")
        if i % 5 == 4:
            print()
        pass

def random_init():
    pass
   


# __name__ ==> "__main__"이 없으면 실행을 시켜줘
if __name__ == " __main__":
    p = create_problem("./data/tsp30.txt")
    describe_problem(p)
    init = random_init(p)
    print(evaluate(init, p))
   
