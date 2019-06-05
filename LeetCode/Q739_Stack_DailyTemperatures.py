# 每日温度
# 根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高的天数。如果之后都不会升高，请输入 0 来代替。
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的都是 [30, 100] 范围内的整数。

class Solution(object):
    # 法一：
    # 从最后一天推到第一天
    def dailyTemperatures1(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        res = [0 for i in range(n)]
        for i in range(n-2, -1, -1):    # 从最后一天推到第一天
            j = i + 1
            while j < n:
                if T[i] < T[j]:             #
                    res[i] = j - i
                    break
                elif res[j] == 0:           #
                    res[i] = 0
                    break
                j += res[j]
        return res

    # 法二：
    # 维护递减栈：后入栈的元素总比栈顶元素小
    # 相当于最好情况的双重for，接近O(n）
    def dailyTemperatures2(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        res = [0 for i in range(n)]
        stack = []  # 用栈记录下遍历过元素的下标，
        for k, v in enumerate(T):
            if stack:
                while stack and T[stack[-1]] < v:
                    res[stack[-1]] = k - stack[-1]
                    stack.pop()
            stack.append(k)
        return res

    def dailyTemperatures(self, T):
        return self.dailyTemperatures2(T)


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))

    # for i in range(3, -1, -1):
    #     print(i)
    #
    # print([0 for i in range(len([1,2,3]))])