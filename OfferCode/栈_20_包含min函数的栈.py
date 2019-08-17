'''
包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''

class Solution:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
    def push(self, node):
        # write code here
        self.main_stack.append(node)
        if not self.min_stack or node < self.min_stack[-1]:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min_stack[-1])
    def pop(self):
        # write code here
        self.min_stack.pop()
        return self.main_stack.pop()
    def top(self):
        # write code here
        return self.main_stack[-1]
    def min(self):
        # write code here
        return self.min_stack[-1]


if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    print(s.top())
    print(s.min())
    s.pop()
    print(s.top())
    print(s.min())

