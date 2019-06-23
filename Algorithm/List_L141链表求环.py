# 环形链表
# 给定一个链表，判断链表中是否有环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

from tool import ListNode, createLinkList

class Solution(object):
    # 用set存储查找
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        listset = set()
        while head:
            if head in listset:
                return True
            listset.add(head)
            head = head.next
        return False
    # 快慢指针
    # 时间复杂度：O(n)，空间复杂度：O(1)
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        fast, slow = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast == None:
                return False
            fast = fast.next
            if slow == fast:
                return True
        return False

    def hasCycle(self, head):
        return self.hasCycle2(head)

if __name__ == '__main__':
    head = createLinkList([i for i in range(8)])
    # head.next.next.next.next.next.next.next = head.next.next
    s = Solution()
    # print(s.hasCycle(head))
    print(s.hasCycle(ListNode(None)))
