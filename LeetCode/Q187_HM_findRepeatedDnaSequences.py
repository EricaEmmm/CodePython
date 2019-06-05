# 重复的DNA序列
# 所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助
# 编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。
#
# 示例:
# 输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出: ["AAAAACCCCC", "CCCCCAAAAA"]

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = dict()
        if len(s) < 10:
            return res
        for i in range(len(s)-9):
            tmp = s[i:i+10]
            res[tmp] = res.get(tmp,0) + 1   # 返回指定键的值，如果值不在字典中返回default值
        return list([i for i in res.keys() if res[i] > 1])



if __name__ == '__main__':
    s = Solution()
    tmp = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(s.findRepeatedDnaSequences(tmp))

    # st = "abc"
    # t = [1,2,3]
    # print(st[0:3])