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
def OutputTreeFront(root):
    if not root:
        return
    print(root.val)
    OutputTreeFront(root.left)
    OutputTreeFront(root.right)


'''
中序遍历：左子树---> 根结点 ---> 右子树
[5, 3, 3, 1, 2, 9]
'''
def OutputTreeMiddle(root):
    if not root:
        return
    OutputTreeMiddle(root.left)
    print(root.val)
    OutputTreeMiddle(root.right)


'''
后序遍历
[5, 3, 3, 9, 2, 1]
'''
def OutputTreeRear(root):
    if not root:
        return
    OutputTreeRear(root.left)
    OutputTreeRear(root.right)
    print(root.val)




'''
层次遍历
[1, 3, 2, 5, 3, 9]
'''
def OutputTreeLevel(root):



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)
    # OutputTreeFront(root)
    # OutputTreeMiddle(root)
    OutputTreeRear(root)