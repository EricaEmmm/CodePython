'''
合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

from tool import ListNode, createLinkList, printList

class Solution(object):
    def mergeTwoLists1(self, l1, l2):
        """
        递归
        时间复杂度：O(m+n),空间复杂度：O(m+n)
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            newHead = l1
            newHead.next = self.mergeTwoLists1(l1.next, l2)
        else:
            newHead = l2
            newHead.next = self.mergeTwoLists1(l1, l2.next)
        return newHead

    def mergeTwoLists2(self, l1, l2):
        """
        迭代
        时间复杂度：O(m+n),空间复杂度：O(1)
        """
        newHead = ListNode(None)
        cur = newHead
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return newHead.next

    def mergeTwoLists(self, l1, l2):
        return self.mergeTwoLists2(l1, l2)

if __name__ == '__main__':
    s = Solution()
    l1 = createLinkList([1,2,4])
    l2 = createLinkList([1,3,4])
    printList(s.mergeTwoLists(l1, l2))
