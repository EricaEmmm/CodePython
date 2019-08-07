#           1
#          / \
#         3   2
#        / \   \
#       5   3   9

from tool import TreeNode

'''
前序遍历：根结点 ---> 左子树 ---> 右子树
[1, 3, 5, 3, 2, 9]
'''
# 递归
def PreOrder(root):
    if not root:
        return
    print(root.val, end=' ')
    PreOrder(root.left)
    PreOrder(root.right)

# 非递归：栈
# 根节点入栈，右子树入栈，左子树入栈，遍历左子树
def PreOrderNor(root):
    if not root:
        return
    sta = []
    sta.append(root)
    while sta:
        tmp = sta.pop()
        print(tmp.val, end=' ')
        if tmp.right:
            sta.append(tmp.right)
        if tmp.left:
            sta.append(tmp.left)


'''
中序遍历：左子树---> 根结点 ---> 右子树
[5, 3, 3, 1, 2, 9]
'''
# 递归
def InOrder(root):
    if not root:
        return
    InOrder(root.left)
    print(root.val, end=' ')
    InOrder(root.right)

# 非递归：栈
# 遍历入栈查找cur为根的最左侧节点，找到后循环跳出
def InOrderNor(root):
    if not root:
        return
    cur = root
    sta = []
    while sta or cur:   # 栈不为空（左子树没遍历完），cur不为空（有右子树）
        # 找最左下的节点，将经过的路径保存
        while cur:
            sta.append(cur)
            cur = cur.left
        # 取栈顶，遍历以cur为根的节点
        cur = sta.pop()
        print(cur.val, end=' ')
        cur = cur.right


'''
后序遍历：左子树 ---> 右子树 ---> 根结点
[5, 3, 3, 9, 2, 1]
'''
# 递归
def PostOrder(root):
    if not root:
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.val, end=' ')

# 非递归：栈
# 遍历入栈查找cur为根的最左侧节点，找到后循环跳出
def PostOrderNor(root):
    if not root:
        return
    cur = root
    sta = []
    top = None
    flag = None
    while sta or cur:   # 栈不为空（左子树没遍历完），cur不为空（有右子树）
        # 找最左下的节点，将经过的路径保存
        while cur:
            sta.append(cur)
            cur = cur.left
        top = sta[-1]
        # 没有右孩子或节点已遍历过
        if not top.right or flag == top.right:
            print(top.val, end=' ')
            flag = top
            sta.pop()
        # 有右孩子，以右孩子为根节点
        else:
            cur = top.right

'''
层次遍历
[1, 3, 2, 5, 3, 9]
'''
# 非递归：队列
def LevelOrder(root):
    if not root:
        return
    que = []
    que.append(root)
    while que:
        tmp = que.pop(0)
        print(tmp.val, end=' ')
        if tmp.left:
            que.append(tmp.left)
        if tmp.right:
            que.append(tmp.right)



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)

    PostOrder(root)