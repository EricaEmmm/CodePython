# 分隔链表
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5


from tool import ListNode, createLinkList, printList

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lesshead = ListNode(None)
        lessptr = lesshead
        morehead = ListNode(None)
        moreptr = morehead
        while head:
            if head.val < x:
                lessptr.next = head
                lessptr = lessptr.next
            else:
                moreptr.next = head
                moreptr = moreptr.next
            head = head.next

        moreptr.next = None # 将链表尾置零，否则若最后一个是比x小的，会导致成为带环链表
        lessptr.next = morehead.next
        return lesshead.next



if __name__ == '__main__':
    head = createLinkList([1,4,3,2,5])
    s = Solution()
    printList(s.partition(head, 3))