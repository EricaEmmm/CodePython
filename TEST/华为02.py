
def find(src, tar):
    n = len(src)
    m = len(tar)
    if n < m:
        return '0'
    for i in range(n):
        for j in range(m):
            if src[(i + j) % n] != tar[j]:
                break
        if j == m-1 and src[(i + j) % n] == tar[j]:
            return '1'
    return '0'


def find2(src, tar):
    n = len(src)
    tmp = src + src
    if tmp.find(tar) != -1:
        return '1'
    return '0'

if __name__ == '__main__':
    # src = []
    # tar = []
    # for i in range(3):
    #     src.append(input())
    #     tar.append(input())
    src = ['AABCD','AABCD','AABCD']
    tar = ['CDAA','ABCD','CFS']
    res = ''
    for i in range(3):
        res += find2(src[i], tar[i])

    print(res)