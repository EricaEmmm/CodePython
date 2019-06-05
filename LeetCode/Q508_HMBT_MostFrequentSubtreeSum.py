# 出现次数最多的子树元素和
# 给出二叉树的根，找出出现次数最多的子树元素和。一个结点的子树元素和定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
# 然后求出出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的元素（不限顺序）。
#
# 示例1
# 输入:
#   5
#  / \
# 2  -3
# 返回[2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。
#
# 示例2
# 输入:
#   5
#  / \
# 2  -5
# 返回[2]，只有2出现两次，-5只出现1次。
# 提示： 假设任意子树元素和均可以用32位有符号整数表示。

from tool import TreeNode

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        map = {}
        def helper(root):
            if not root:
                return 0
            tmp = root.val + helper(root.left) + helper(root.right)
            map[tmp] = map.get(tmp, 0) + 1
            return tmp
        helper(root)
        max_sum = 0
        for k,v in map.items():
            if v > max_sum:
                max_sum = v
                res.clear() # or res[:] = []，python3.3后才有.clear()
                res.append(k)
            elif v == max_sum:
                res.append(k)
        return res

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(-5)
    s = Solution()
    print(s.findFrequentTreeSum(root))


