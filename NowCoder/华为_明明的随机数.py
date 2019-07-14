if __name__ == '__main__':
    # 循环输入
    while True:
        try:
            n = int(input())
            list_in = []
            for i in range(n):
                list_in.append(int(input()))
            for i in sorted(set(list_in)):
                print(i)
        except:
            break