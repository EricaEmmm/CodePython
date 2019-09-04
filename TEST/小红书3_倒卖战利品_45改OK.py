'''
倒卖战利品
在游戏中，击败魔物后，薯队长获得了N件宝物，接下来得把这些宝物卖给宝物回收员来赚点小钱。
这个回收员有个坏毛病，每次卖给他一件宝物后，之后他就看不上比这件宝物差的宝物了。
在这个世界中，衡量宝物的好坏有两个维度，稀有度X和实用度H，回收员在回收一个宝物A后，
下一个宝物的稀有度和实用度都不能低于宝物A。那么薯队长如何制定售卖顺序，才能卖给回收员宝物总个数最多。
输入
第一行一个正整数N。
接下来N行。每行两个整数分别表示X 和 H
X1 H1
X2 H2
…
XN HN
输出
一个整数，表示最多可以卖出的宝物数
样例输入
4
3 2
1 1
1 3
2 2
样例输出
3
'''
def helper1(nums):
    dp = [1 for i in range (len(nums))]
    maxRes = 0
    for i in range(1, len(nums)):
        for j in range(0, i):
            if (nums[j] <= nums[i]):
                dp[i] = max(dp[i], dp[j]+1)
            maxRes = max(dp[i], maxRes)
    return maxRes

def helper2(nums):
    if not nums:
        return 0
    dp = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] >= dp[-1]:
            dp.append(nums[i])
        else:
            l, r= 0, len(dp)-1
            while l < r:
                mid = (l + r) // 2
                if nums[i] > dp[mid]:
                    l = mid + 1
                else:
                    r = mid
            dp[l] = nums[i]
    return len(dp)

if __name__ == '__main__':
    n = int(input())
    tmp = []
    for i in range(n):
        tmp.append(list(map(int, input().split())))

    tmp.sort()
    nums = []
    for i in range(n):
        nums.append(tmp[i][1])
    print(helper2(nums))