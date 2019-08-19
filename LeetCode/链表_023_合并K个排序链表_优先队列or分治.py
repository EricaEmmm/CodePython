'''
合并K个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''

from tool import ListNode, createLinkList, printList

'''
复杂度分析（假设K个链表，所有链表总共N个节点）
暴力：所有链表节点放到一个数组中，排序，再创建新链表
    时间：O(NlogN)，空间：O(N)
逐一比较：比较每个链表首节点，最小的放到最终有序链表尾部。几乎每个节点都要比较K-1次
    时间：O(NK)，空间：O(1)
优先队列：比较环节用优先队列（最小堆）优化，比较代价O(logK)
    时间：O(NlogK)，空间：O(K)
分治：将K个链表一直对半分，向上两两合并。每次合并都要遍历几乎全部N个节点，合并logK次
    时间：O(NlogK)，空间：O(NlogK)
'''

class Solution(object):
    '''
    分治
    时间复杂度：O(NlogK)
    '''
    def mergeKLists1(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l1 = self.mergeKLists1(lists[:mid])
        l2 = self.mergeKLists1(lists[mid:])
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            newHead = l1
            newHead.next = self.mergeTwoLists(l1.next, l2)
        else:
            newHead = l2
            newHead.next = self.mergeTwoLists(l1, l2.next)
        return newHead

    '''
    优先队列
    时间复杂度：O(NlogK)
    '''
    def mergeKLists2(self, lists):
        from queue import PriorityQueue
        que = PriorityQueue()
        # 建立头结点优先队列
        x = 0
        for i in lists:
            if i:
                que.put((i.val, x, i))    # 比较tuple成员，若第一项相同，则会比较下一项。而ListNode没有比较方法，py3就会抛出异常。添加x，使比较继续。
                x += 1
        # 构建新有序链表
        head = ptr = ListNode(None)
        while not que.empty():
            val, x, idx = que.get()
            ptr.next = idx
            ptr = ptr.next
            idx = idx.next
            if idx:
                que.put((idx.val, x, idx))
        return head.next

    '''
    最小堆
    时间复杂度：O(NlogK)
    '''
    def mergeKLists3(self, lists):
        import heapq
        small = []
        # 建立头结点最小堆
        x = 0
        for i in lists:
            if i:
                heapq.heappush(small, (i.val, x, i))    # 比较tuple成员，若第一项相同，则会比较下一项。而ListNode没有比较方法，py3就会抛出异常。添加x，使比较继续。
                x += 1
        # 构建新有序链表
        head = ptr = ListNode(None)
        while small:
            val, x, idx = heapq.heappop(small)
            ptr.next = idx
            ptr = ptr.next
            idx = idx.next
            if idx:
                heapq.heappush(small, (idx.val, x, idx))
        return head.next

    def mergeKLists(self, lists):
        return self.mergeKLists3(lists)


if __name__ == '__main__':
    s = Solution()
    l1 = createLinkList([1, 4, 5])
    l2 = createLinkList([1, 3, 4])
    l3 = createLinkList([2, 6])
    printList(s.mergeKLists([l1,l2,l3]))
