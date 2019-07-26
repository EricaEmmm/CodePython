# 用两个栈来实现队列
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。


class Solution:
    # def __init__(self):
    #     self.queue = []
    #     self.tmp = []
    #
    # def push(self, node):
    #     while self.queue:
    #         self.tmp.append(self.queue.pop())
    #     self.queue.append(node)
    #     while self.tmp:
    #         self.queue.append(self.tmp.pop())
    #
    # def pop(self):
    #     return self.queue.pop()

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack2) != 0:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(4)
    s.push(3)
    print(s.pop())
    print(s.pop())