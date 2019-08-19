# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkList(List):
    """
    :type List: list/str
    :rtype: ListNode
    """
    if len(List) <= 0:
        return None
    linkList = ListNode(None)
    pNode = linkList

    for i in List:
        node = ListNode(i)
        pNode.next = node
        pNode = pNode.next

    return linkList.next

def printList(head):
    """
    :type head: ListNode
    """
    res = ""
    while head:
        res = res + str(head.val) + " -> "
        head = head.next
    res = res + "None"
    print(res)


# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


# 最小堆
import heapq
class SmallHeap(object):
    def __init__(self):
        self.arr = list()

    def heap_push(self, val):   # 使用一个空列表，把值加入堆中
        heapq.heappush(self.arr, val)

    def heapify(self, list):    # 转换列表成为堆结构
        heapq.heapify(list)

    def heap_pop(self):
        return heapq.heappop(self.arr)

    def heap_pushpop(self, val):# 先执行了heappush,然后执行了heappop
        return heapq.heappushpop(self.arr, val)

    def heap_replace(self, val):# 先执行了heappop,然后执行了heappush
        return heapq.heapreplace(self.arr, val)

    def get_top(self):
        if not self.arr:
            return
        return self.arr[0]

# 最大堆
class BigHeap:
    def __init__(self, arr = []):
        self.arr = [-i for i in arr]

    def heap_push(self, val):
        heapq.heappush(self.arr, -val)

    def heapify(self):    # 转换列表成为堆结构
        heapq.heapify(self.arr)

    def heap_pop(self):
        return -heapq.heappop(self.arr)

    def heap_pushpop(self, val):
        return heapq.heappushpop(self.arr, -val)

    def heap_replace(self, val):
        return heapq.heapreplace(self.arr, -val)

    def get_top(self):
        if not self.arr:
            return
        return -self.arr[0]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def OutputTree(self, tree):
    #     """
    #     :type tree: List[TreeNode]
    #     :rtype res: List[str]
    #     """
    #     if tree == None:
    #         return
    #     queue = []
    #     while()

    def OutputTreeFront(self, root, res):
        """
        先序遍历：根结点 ---> 左子树 ---> 右子树
        """
        if root == None:
            return
        res.append(root.val)
        self.OutputTreeFront(root.left, res)
        self.OutputTreeFront(root.right, res)

    def OutputTreeMiddle(self, root, res):
        """
        中序遍历：左子树---> 根结点 ---> 右子树
        """
        if root == None:
            return
        self.OutputTreeMiddle(root.left, res)
        res.append(root.val)
        self.OutputTreeMiddle(root.right, res)

    def OutputTreeRear(self, root, res):
        """
        后序遍历：左子树 ---> 右子树 ---> 根结点
        """
        if root == None:
            return
        self.OutputTreeRear(root.left, res)
        self.OutputTreeRear(root.right, res)
        res.append(root.val)

    def OutputTreeLevel(self, root, res):
        """
        层次遍历
        """
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

    def treeNodeToString(self, root):
        if not root:
            return "[]"
        output = ""
        queue = [root]
        current = 0
        while current != len(queue):
            node = queue[current]
            current = current + 1

            if not node:
                output += "null, "
                continue

            output += str(node.val) + ", "
            queue.append(node.left)
            queue.append(node.right)
        return "[" + output[:-2] + "]"

    def treeNodeArrayToString(self, treeNodeArray):
        serializedTreeNodes = []
        for treeNode in treeNodeArray:
            serializedTreeNode = self.treeNodeToString(treeNode)
            serializedTreeNodes.append(serializedTreeNode)
        return "[{}]".format(', '.join(serializedTreeNodes))


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def InputIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[Interval]
        """
        res = []
        for i in intervals:
            res.append(Interval(i[0],i[1]))
        return res

    def OutputIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[List[int]]
        """
        res = []
        for i in intervals:
            res.append([i.start, i.end])
        print(res)



if __name__ == '__main__':
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # test = Interval()
    # test.OutputIntervals(test.InputIntervals(intervals))

    s = TreeNode(2)
    s.left = TreeNode(1)
    s.right = TreeNode(3)
    res = []
    s.OutputTreeLevel(s, res)
    print(res)