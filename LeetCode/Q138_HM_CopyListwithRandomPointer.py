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

from tool import Node,TreeNode
# import copy

class Solution(object):
    def copyRandomList1(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #法一：
        # return copy.deepcopy(head)    # 调用深拷贝函数

        #法二：有丝分裂法，原地复制再分裂，时间O(3n)，空间O(1)
        if not head:
            return None

        tmp = head
        while tmp:  # 将拷贝节点放置该结点后面
            copy = Node(tmp.val, tmp.next, None)
            tmp.next = copy
            tmp = copy.next

        tmp = head
        while tmp:  # 将源节点的random指针赋给拷贝节点
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next

        tmp = head.next
        while head:  # 将源链表与拷贝链表分离
            copy = head.next
            head.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            head = head.next

        return res

    def copyRandomList2(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 法三：HashMap实现
        if not head:
            return None

        map = dict()
        tmp = head
        while tmp:
            copy = Node(tmp.val, None, None)
            map[tmp] = copy
            tmp = tmp.next

        tmp = head
        while tmp:
            copy = map[tmp]
            if tmp.next:
                copy.next = map[tmp.next]
            if tmp.random:
                copy.random = map[tmp.random]
            tmp = tmp.next
        return map[head]

    def copyRandomList(self, head):
        return self.copyRandomList2(head)

def OutputTreeFront(root, res):
    """
    先序遍历：根结点 ---> 左子树 ---> 右子树
    """
    if root == None:
        return
    res.append(root.val)
    OutputTreeFront(root.left, res)
    OutputTreeFront(root.right, res)


if __name__ == '__main__':
    s = Solution()
    root = Node(1,None,None)
    root.next = Node(2,None,None)
    root.random = root.next
    root.next.random = root.next

    t = s.copyRandomList(root)

    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    #
    # tmp = root
    # node = TreeNode(tmp.val)
    # node.left = tmp.left
    # # tmp.left = node
    # tmp = node.left
    # res=[]
    # OutputTreeFront(tmp, res)
    # print(res)

    # a=[1,2,3]
    # b=a
    # b.append(4)
    # print(a)



