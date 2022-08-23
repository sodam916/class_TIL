#
def to_post(data):

# 중위표기식 data를 읽어서 후위표기식 문자열로 반환하는 함수
# 피연산자이면 result에 더하기
# 연산자이면, stack push
#   단, 나보다 우선순위가 높거나 같은애들은 다빼고 push
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    stack = []
    result = ''
    for i in range(len(data)):
        if data[i] in '+-*/()':
            if not stack:
                stack.append(data[i])
            else:
                # ) vs 나머지 : )는 스택에 안들어가기 때문에..
                if data[i] == ')':
                    #여는 괄호가 나올때 까지 pop하면서 연산자 출력, 여는 괄호는 pop하고 버리기
                    while stack[-1] != '(':
                        result += stack.pop()
                    stack.pop() #여는 괄호 버리기
                else:   # +-*/( 인경우

                    while stack and isp[stack[-1]] >= icp[data[i]]:
                        result += stack.pop()
                    stack.append(data[i])
        else:
            result += data[i]
    #스택에 남아있는 연산자들 모조리 꺼내서 붙여주기
    while stack:
        result += stack.pop()

    return result
#후위 표기식을 계산하는 함수 작성
def calculate(data):

# 피연산자는 스택에다가 넣기
# 연산자가 나오면, 피연산자 두 개 빼서 연산하고 다시 스택에 넣기
    stack = []
    for i in range(len(data)):
        if data[i] in '+-*/':
            num2 = stack.pop()
            num1 = stack.pop()
            if data[i] == '+':
                stack.append(num1+num2)
            elif data[i] == '-':
                stack.append(num1 - num2)
            elif data[i] == '*':
                stack.append(num1 * num2)
            elif data[i] == '/':
                stack.append(num1 // num2)
        else:
            stack.append(int(data[i]))
    return stack.pop()