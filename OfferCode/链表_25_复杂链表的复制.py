'''
复杂链表的复制
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:       # 注意！！！
            return None
        # 复制next
        cur = pHead
        while cur:
            copy = RandomListNode(cur.label)
            copy.next = cur.next
            cur.next = copy
            cur = cur.next.next
        # 复制random
        cur = pHead
        while cur:
            if cur.random:  # 注意！！！
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分
        newHead = pHead.next
        copy = newHead
        cur = pHead
        while cur:
            cur.next = copy.next
            if copy.next:   # 注意！！！
                copy.next = copy.next.next
            cur = cur.next
            copy = copy.next
        return newHead

if __name__ == '__main__':
    s = Solution()
    root = RandomListNode(1)
    root.next = RandomListNode(2)
    root.random = root.next
    root.next.random = root.next

    t = s.Clone(root)

