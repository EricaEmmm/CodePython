'''
加密：二进制数B（明文），长度N，该信息被写下K次，每次向右移0,1...K-1位，然后对每列按异或，得到S（密文）
输入：第一行N、K，第二行S
输出：明文B
示例1：
输入：
7 4
1110100110
输出：
1001010
'''

if __name__ == '__main__':
    N, K = [7,4]    #list(map(int, input().split()))  #
    S = '1110100110' #input() #

    # res = [0 for i in range(N)]
    # res[0] = int(S[0])
    # for i in range(1, N):
    #     res[i] = int(S[i])
    #     for j in range(i-1, max(-1, i-K), -1):
    #        res[i] ^= res[j]

    # res = [0 for i in range(N)]
    # for i in range(0, N):
    #     res[i] ^= int(S[i])
    #     if i >= K:
    #         res[i] ^= res[i-K]
    #     if i < N-1:
    #         res[i+1] = res[i]
    #         res[i+1] ^= int(S[i])
    #         res[i+1] ^= res[i]

    res = [0 for i in range(K+1)]
    for i in range(0, N):
        res[-1] ^= int(S[i])
        if i >= K:
            res[-1] ^= res[-1-K]
        print(res[-1], end='')
        del res[0]
        if i < N-1:
            res.append(res[-1])
            res[-1] ^= int(S[i])
            res[-1] ^= res[-2]
        else:
            res.append(0)
