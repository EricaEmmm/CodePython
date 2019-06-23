# 复制带随机指针的链表
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 要求返回这个链表的“深拷贝”。
# 输入：
# {"$id": "1", "next": {"$id": "2", "next": null, "random": {"$ref": "2"}, "val": 2}, "random": {"$ref": "2"}, "val": 1}
#
# 解释：
# 节点1的值是1，它的下一个指针和随机指针都指向节点2 。
# 节点2的值是2，它的下一个指针指向null，随机指针指向它自己。
#
# 提示：
# 你必须返回给定头的拷贝作为对克隆列表的引用。

from tool import Node

class Solution(object):
    # HashMap
    def copyRandomList1(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        nodemap = {}
        ptr = head
        while ptr:
            nodemap[ptr] = Node(ptr.val, None, None)
            ptr = ptr.next

        ptr = head
        while ptr:
            if ptr.next:
                nodemap[ptr].next = nodemap[ptr.next]
            if ptr.random:
                nodemap[ptr].random = nodemap[ptr.random]
            ptr = ptr.next

        return nodemap[head]

    # 原地分裂
    def copyRandomList2(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        ptr = head
        while ptr:              # 将拷贝节点放置该结点后面
            copy = Node(ptr.val, None, None)
            next = ptr.next
            ptr.next = copy
            copy.next = next
            ptr = ptr.next.next

        ptr = head
        while ptr:              # 将源节点的random指针赋给拷贝节点
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next

        new_head = head.next
        ptr = head
        while ptr:
            copy = ptr.next     # 将源链表与拷贝链表分离
            ptr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            ptr = ptr.next

        return new_head

    def copyRandomList(self, head):
        return self.copyRandomList2(head)


if __name__ == '__main__':
    s = Solution()
    root = Node(1,None,None)
    root.next = Node(2,None,None)
    root.random = root.next
    root.next.random = root.next

    t = s.copyRandomList(root)