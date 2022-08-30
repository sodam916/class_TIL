word = ['MHYUMBOCNQLABALQNSZWIOBINM']
N = 26
M = 7
for w in word:
    wl = list(w)
lst = []
com = []
for s in range(0, N - M + 1):
    e = s + M - 1
    for i in range(s, s+M):
        lst.append(wl[i])
        com.append(wl[i])
    print(com)
    # for n in range(M//2):
    #     lst[n], lst[M-1-n] = lst[M-1-n], lst[n]
    #
    # if com == lst:
    #     print(com)
    #     break
    # else:
    #     lst = []
    #     com = []
    #

    # if lst == lst[::-1]:
    #     print(0)
    #     break
    # else: lst = []









        # for n in range(M//2):
        #     word[n], word[M-1-n] = word[M-1-n], word[n]
        #
        # if i in word[n]:
        #     print(i)