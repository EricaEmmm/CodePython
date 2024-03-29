# 最小栈
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#     push(x) -- 将元素 x 推入栈中。
#     pop() -- 删除栈顶的元素。
#     top() -- 获取栈顶元素。
#     getMin() -- 检索栈中的最小元素。
#
# 示例:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        elif x < self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-1)
    obj.push(-2)
    obj.push(3)
    obj.push(4)
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())
