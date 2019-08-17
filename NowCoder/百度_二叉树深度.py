from tool import TreeNode

def depth(root):
    # 递归
    if not root:
        return 0
    return max(depth(root.left), depth(root.right)) + 1

def depth1(root):
    # 层次遍历：队列
    depth = 0
    tmp = []
    tmp.append(root)
    while tmp:
        depth += 1
        for i in range(len(tmp)):
            new = tmp[0]
            del tmp[0]
            if new.left:
                tmp.append(new.left)
            if new.right:
                tmp.append(new.right)
    return depth


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    print(depth(root))