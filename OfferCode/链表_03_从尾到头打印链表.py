# 从尾到头打印链表
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

from tool import ListNode,createLinkList

class Solution:
    def printListFromTailToHead1(self, listNode):
        array = []
        head = listNode
        while head:
            array.append(head.val)
            head = head.next
        n = len(array)
        left, right = 0, n-1
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        return array

    def printListFromTailToHead2(self, listNode):
        """
        列表插入
        """
        array = []
        while listNode:
            array.insert(0, listNode.val)
            listNode = listNode.next
        return array

    def printListFromTailToHead(self, listNode):
        return self.printListFromTailToHead2(listNode)


if __name__ == '__main__':
    s = Solution()
    listNode = createLinkList([1,2,5,4,7])
    print(s.printListFromTailToHead(listNode))

