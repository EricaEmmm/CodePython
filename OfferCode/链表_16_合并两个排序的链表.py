'''
合并两个排序的链表
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

from tool import ListNode, createLinkList, printList

class Solution:
    # 返回合并后列表
    def Merge1(self, pHead1, pHead2):
        # 循环
        dummy = ListNode(None)
        tail = dummy
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                tail.next = pHead1
                tail = tail.next
                pHead1 = pHead1.next
            else:
                tail.next = pHead2
                tail = tail.next
                pHead2 = pHead2.next
        if pHead1 != None:
            tail.next = pHead1
        if pHead2 != None:
            tail.next = pHead2
        return dummy.next

    def Merge2(self, pHead1, pHead2):
        # 递归
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        dummy = None
        if pHead1.val < pHead2.val:
            dummy = pHead1
            dummy.next = self.Merge2(pHead1.next, pHead2)
        else:
            dummy = pHead2
            dummy.next = self.Merge2(pHead1, pHead2.next)
        return dummy

    def Merge(self, pHead1, pHead2):
        return self.Merge2(pHead1, pHead2)

if __name__ == '__main__':
    s = Solution()
    pHead1 =createLinkList([1,3,5])
    pHead2 =createLinkList([2,4,5])
    printList(s.Merge(pHead1, pHead2))
