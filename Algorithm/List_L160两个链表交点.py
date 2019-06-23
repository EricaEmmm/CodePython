# 相交链表
# 编写一个程序，找到两个单链表相交的起始节点
#
# 示例1:
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：
# 相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：
# 从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
# 由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
# 这两个链表不相交，因此返回 null。


from tool import ListNode, createLinkList, printList

class Solution(object):
    # 用set存储查找
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeset = set()
        while headA != None:    # 将链表A的元素插入set中
            nodeset.add(headA)
            headA = headA.next
        while headB != None:    # 检查链表B的元素是否在set中
            if headB in nodeset:
                return headB
            headB = headB.next
        return None

    # 先行法，对齐链表
    # 时间复杂度：O(n)，空间复杂度：O(1)
    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 遍历计算链表A、B的长度
        lenA, lenB = 0, 0
        tmpA, tmpB = headA, headB
        while tmpA != None:
            lenA += 1
            tmpA = tmpA.next
        while tmpB != None:
            lenB += 1
            tmpB = tmpB.next

        # 将 较长链表指针 对齐到 较短链表头结点
        if lenB > lenA:
            for i in range(lenB-lenA):
                headB = headB.next
        else:
            for i in range(lenA-lenB):
                headA = headA.next

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    # 定义两个指针, 第一轮让两个到达末尾的节点指向另一个链表的头部, 最后如果相遇则为交点(在第一轮移动中恰好抹除了长度差)
    # 两个指针等于移动了相同的距离, 有交点就返回, 无交点就是各走了两条指针的长度
    # 时间复杂度：O(n)，空间复杂度：O(1)
    def getIntersectionNode3(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa, pb = headA, headB
        # 在这里第一轮体现在pa和pb第一次到达尾部会移向另一链表的表头, 而第二轮体现在如果pa或pb相交就返回交点, 不相交最后就是None == None
        while pa != pb:
            pa = headB if (pa == None) else pa.next
            pb = headA if (pb == None) else pb.next
        return pa

    def getIntersectionNode(self, headA, headB):
        return self.getIntersectionNode3(headA, headB)

if __name__ == '__main__':
    headA = createLinkList([4,1])
    headB = createLinkList([5,0,1])
    headC = createLinkList([8,4,5])
    headA.next.next = headC
    headB.next.next.next = headC
    s = Solution()
    printList(s.getIntersectionNode(headA, headB))

    # t = set()
    # t.add(1)
    # t.add(2)
    # t.add(2)
    # print(t)
    # print(1 in t)
