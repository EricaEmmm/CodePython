# 反转链表
# 反转一个单链表。
#
# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

from tool import ListNode, createLinkList, printList

class Solution(object):
    # 头插法迭代
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        new_head = None
        while head:
            next = head.next        # 临时节点，暂存当前节点的下一节点
            head.next = new_head    # 原地逆置
            new_head = head         # 新头结点前移
            head = next             # 原头结点后移

        return new_head

    def reverseList(self, head):
        return self.reverseList1(head)


if __name__ == '__main__':
    head = createLinkList("12345")
    s = Solution()
    printList(s.reverseList(head))

