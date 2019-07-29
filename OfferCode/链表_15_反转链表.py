# 反转链表
# 输入一个链表，反转链表后，输出新链表的表头。

from tool import ListNode, createLinkList, printList
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # 头插法迭代
        newHead = None

        while pHead:
            next = pHead.next       # 临时节点，暂存当前节点的下一节点
            pHead.next = newHead    # 原地逆置
            newHead = pHead         # 新头结点前移
            pHead = next            # 原头结点后移
        return newHead

if __name__ == '__main__':
    s = Solution()
    ll = createLinkList([1,2,3])
    printList(s.ReverseList(ll))