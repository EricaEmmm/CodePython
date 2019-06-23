# 验证栈序列
# 给定pushed和popped两个序列，只有当它们可能是在最初空栈上进行的推入push和弹出pop操作序列的结果时，返回true；否则，返回false 。
#
# 示例1：
# 输入：pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#
# 示例2：
# 输入：pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]
# 输出：false
# 解释：1不能在2之前弹出。
#
# 提示：
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed是popped的排列。

class Solution(object):
    # 贪心
    # 用一个栈把 pushed 数组里的数依次 push 进去，push 之后检查栈顶的数是否等于 popped 的头元素，如果相等则去掉头元素。
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []  # 临时栈
        while pushed:
            stack.append(pushed[0])
            # pushed = pushed[1:]
            del pushed[0]
            while stack != [] and stack [-1] == popped[0]:  # popped序列为队列，队列首部与临时栈栈顶相同，则弹出
                stack.pop()
                # popped = popped[1:]
                del popped[0]
        return False if stack else True


if __name__ == '__main__':
    s = Solution()
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    print(s.validateStackSequences(pushed, popped))


