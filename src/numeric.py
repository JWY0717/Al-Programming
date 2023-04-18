
# random
import random

# 간단한 언덕 등반 알고리즘
## <=> Convex.txt 를 사용해서 계산을 하자

## 1. 파일을 읽어 보자
## 2.파일 읽었음
## 3. Convex.txt 파일의 수식과 값을 이용해서 계산



def create_problem(fileanme):
    # 숫자
    # Convex.txt의 1번줄과 2~6번나머지 줄의 형태가 다름
    
    # 1-1. 파일을 읽자 = fileanme, 'r'  =>
    ini_file = open(fileanme, 'r')
    expression =  ini_file.readline().strip()
    
    var_names = []
    low = []
    up = []
    
    for line in ini_file.readlines():
        # n,l,u = tuple(line.split(","))
        
        var_names.append(line.split(",")[0])
        low.append(float(line.split(",")[1]))
        up.append(float(line.split(",")[2]))
    
    ini_file.close()
    domain = [var_names, low, up]
    return (expression, domain)

def random_init(p):
    expression, domain = p
    init = []
    for i in range(0, len(domain[0])):
        init.append(random.uniform(domain[1][i],domain[2][i]))
    return init

def evaluate(state, p):
    #초기값 설정
    num_eval = 0
    expression =  p[0]
    var_name = p[1][0]
    
    for i in range(len(var_name)):
        # assignment = 할당분 ,,, exec=> 문자열을 파이썬 코드로 실행하는 것 ~
        assignment = var_name[i] + '=' + str(state[i])
        exec(assignment)
        
        
    return eval(expression)
         

# __name__ ==> "__main__"이 없으면 실행을 시켜줘
if __name__ == " __main__":
    # 식과 인자를 분리
    p = create_problem("./data/Convex.txt")
    describe_problem(p)
    solution = random_init(p)
    minimum = evaluate(solution, p)
    print(f"{minimum}")


## 2.
## 3.
## 4.

