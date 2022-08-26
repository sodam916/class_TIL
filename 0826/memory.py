T = int(input())

for tc in range(1, T+1):
    memory = list(map(int, input().strip()))
    lst = 0
    for n in range(len(memory)):
        if memory[n] == 1:
            for i in range(n+1,len(memory)):
                if memory[i] == '0':
                    memory[i] = 1
                elif memory[i] == '1':
                    memory[i] = 0


    print(memory, lst)

