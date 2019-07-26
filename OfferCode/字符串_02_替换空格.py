# 替换空格
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

class Solution:
    def replaceSpace1(self, s):
        """
        顺序查找替换
        :param s: 源字符串
        :return: 替换空格字符串
        """
        res = ''
        for i in s:
            if i == ' ':
                res += '%20'
            else:
                res += i
        return res

    def replaceSpace2(self, s):
        """
        调用API
        :param s: 源字符串
        :return: 替换空格字符串
        """
        return s.replace(' ', '%20')

    def replaceSpace3(self, s):
        """
        双指针，从字符串的尾部开始复制和替换
        时间复杂度：O(n)，空间复杂度：O(1)
        :param s: 源字符串
        :return: 替换空格字符串
        """
        # 字符串转数组
        str = []
        spacelen = 0
        for i in s:
            str.append(i)
            if i == ' ':
                spacelen += 1
        if spacelen == 0:
            return s

        for i in range(spacelen*2):
            str.append('')

        ptrhead = len(s) - 1
        ptrrear = len(str)-1
        while ptrhead >= 0:
            if str[ptrhead] != ' ':
                str[ptrrear] = str[ptrhead]
                ptrrear -= 1
                ptrhead -= 1
            else:
                str[ptrrear-2:ptrrear+1] = '%20'
                ptrrear -= 3
                ptrhead -= 1

        # 数组转字符串
        s = ''.join(str)
        return s

    def replaceSpace(self, s):
        return self.replaceSpace3(s)

if __name__ == '__main__':
    s = Solution()
    str = 'We Are Happy'

    # str = str.replace(str[0], str[1])
    # print(str)

    # s=['1','2','3']
    # for i in range(2):
    #     s.append('')
    # print(s)

    print(s.replaceSpace(str))