# 用队列实现栈
# 使用队列实现栈的下列操作：
#     push(x) -- 元素 x 入栈
#     pop() -- 移除栈顶元素
#     top() -- 获取栈顶元素
#     empty() -- 返回栈是否为空
#
# 注意:
#     你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
#     你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
#     你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

# 双队列实现
from queue import Queue
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = Queue()
        self.tmp_queue = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.tmp_queue.put(x)
        while not self.stack.empty():
            self.tmp_queue.put(self.stack.get())
        while not self.tmp_queue.empty():
            self.stack.put(self.tmp_queue.get())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        top = self.stack.get()
        self.tmp_queue.put(top)
        while not self.stack.empty():
            self.tmp_queue.put(self.stack.get())
        while not self.tmp_queue.empty():
            self.stack.put(self.tmp_queue.get())
        return top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.stack.empty()

# 列表实现
class MyStack1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if len(self.stack) else True

if __name__ == '__main__':
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.pop())
    print(obj.top())
    print(obj.empty())


