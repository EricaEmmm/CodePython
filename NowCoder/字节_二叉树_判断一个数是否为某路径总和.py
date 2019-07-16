# 判断一个数是否为二叉树的路径节点值之和
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
# True
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
from tool import TreeNode

def dfs(root, target, trace, res):
    if not root:
        return
    trace.append(root.val)

    dfs(root.left, target, trace[:], res)
    if sum(trace) == target:
        res.append(trace)

    dfs(root.right, target, trace[:], res)
    if sum(trace) == target:
        res.append(trace)

def dfs1(root, target, trace, res):
    trace.append(root.val)
    if root.left == None and root.right == None and sum(trace) == target:
        res.append(trace)

    if root.left:
        dfs1(root.left, target, trace[:], res)
    if root.right:
        dfs1(root.right, target, trace[:], res)

def pathSum(root, target):
    if not root:
        return False
    res = []
    dfs1(root, target, [], res)
    return True if len(res) else False

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print(pathSum(root, 22))