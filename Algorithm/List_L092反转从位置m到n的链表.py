# 反转链表 II
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

from tool import ListNode, createLinkList, printList

class Solution(object):
    def reverseBetween1(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 记录逆置开始节点M的前驱节点
        if m > 1:
            preNodeM = head
            for i in range(m-2):
                preNodeM = preNodeM.next
            myhead = preNodeM.next
        else:
            myhead = head

        new_head = None
        new_tail = myhead       # 指向逆转前的链表头部，即逆转后的链表尾部
        for i in range(n-m+1):
            next = myhead.next      # 临时节点，暂存当前节点的下一节点
            myhead.next = new_head  # 原地逆置
            new_head = myhead       # 新头结点前移
            myhead = next           # 原头结点后移

        new_tail.next = myhead  # 将逆转后的链表尾部 与 逆置段的后一个节点相连
        if m > 1:               # 将逆置段的前一个节点 与 逆转后的链表头部相连
            preNodeM.next = new_head
            return head
        else:
            return new_head

    def reverseBetween2(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        # 哑结点
        dummy = ListNode(None)
        dummy.next = head

        preNodeM = dummy
        for i in range(m-1):
            preNodeM = preNodeM.next
        head = preNodeM.next

        new_head = None
        new_tail = head
        for i in range(n-m+1):
            next = head.next
            head.next = new_head
            new_head = head
            head = next

        preNodeM.next = new_head    # 将逆置段的前一个节点 与 逆转后的链表头部相连
        new_tail.next = head        # 将逆转后的链表尾部 与 逆置段的后一个节点相连
        return dummy.next

    def reverseBetween(self, head, m, n):
        return self.reverseBetween2(head, m, n)

if __name__ == '__main__':
    head = createLinkList("12345")
    s = Solution()
    printList(s.reverseBetween(head, 2, 2))