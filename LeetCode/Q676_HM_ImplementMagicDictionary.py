# 实现一个魔法字典
# 实现一个带有buildDict, 以及 search方法的魔法字典。
# 对于buildDict方法，你将被给定一串不重复的单词来构建一个字典。
# 对于search方法，你将被给定一个单词，并且判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。
#
# 示例 1:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
#
# 注意:
#     你可以假设所有输入都是小写字母 a-z。
#     为了便于竞赛，测试所用的数据量很小。你可以在竞赛结束后，考虑更高效的算法。
#     请记住重置MagicDictionary类中声明的类变量，因为静态/类变量会在多个测试用例中保留。 请参阅这里了解更多详情。


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in dict:
            self.map[word] = self.map.get(word, 0)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        flag = 0
        for k in self.map.keys():
            if len(k) != len(word):
                continue
            cnt = 0
            for i in range(len(k)):
                if k[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                flag = 1
        if flag:
            return True
        else:
            return False

if __name__ == '__main__':
    obj = MagicDictionary()
    obj.buildDict(["hello", "hallo", "leetcode"])
    print(obj.search("hello"))
    print(obj.search("hallo"))
    print(obj.search("hell"))
    print(obj.search("leetcoded"))