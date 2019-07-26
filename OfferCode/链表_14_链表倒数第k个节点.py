# 链表中倒数第k个节点
# 输入一个链表，输出该链表中倒数第k个结点。

from tool import createLinkList

class Solution:
    def FindKthToTail1(self, head, k):
        """
        双指针
        时间复杂度：O(n),空间复杂度：O(1)
        """
        if not head or k == 0:
            return
        # right指针向前走k-1，left指针保持不动
        left, right = head, head
        i = k-1
        while i:
            if right.next:
                right = right.next
                i -= 1
            else:
                return
        # right指针走到尾结点，left指针即为倒数第k个结点
        while right.next:
            right = right.next
            left = left.next
        return left

    def FindKthToTail2(self, head, k):
        """
        列表存储
        时间复杂度：O(n),空间复杂度：O(n)
        """
        if not head or k == 0:
            return
        res = []
        while head:
            res.append(head)
            head = head.next
        if len(res) >= k:
            return res[len(res)-k]

    def FindKthToTail(self, head, k):
        return self.FindKthToTail1(head, k)

if __name__ == '__main__':
    s = Solution()
    head = createLinkList([1,2,3,4,5])
    print(s.FindKthToTail(head, 1))

