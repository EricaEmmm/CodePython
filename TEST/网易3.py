def main():
    n = int(input())
    array = list(map(int, input().split()))
    for i in range(n):
        minIndex = i
        for j in range(i, n):
            if array[j] < array[minIndex]:
                minIndex = j
        if minIndex > i:
            array[i], array[minIndex] = array[minIndex], array[i]
    print(' '.join(map(str, array)))

main()