
if __name__ == '__main__':
    n, m, k = list(map(int, input().split()))
    nums = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            nums.append(i*j)
    nums.sort(reverse=True)
    print(nums[k-1])