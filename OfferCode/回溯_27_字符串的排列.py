'''
字符串的排列
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''

class Solution:
    def Permutation(self, ss):
        res = []
        if len(ss) < 1:
            return res
        self.backtrack(ss, '', res)
        res = list(set(res))
        return sorted(res)

    # def backtrack(self, choice, track, res):
    #     '''
    #     不重复元素的全排列
    #     '''
    #     if len(track) == len(choice):
    #         res.append(track)
    #         return
    #     for i in range(len(choice)):
    #         # choose
    #         if choice[i] in track:
    #             continue
    #         track += choice[i]
    #         # next decision
    #         self.backtrack(choice, track, res)
    #         #unchoose
    #         track = track[:-1]

    def backtrack(self, choice, track, res):
        if len(choice) == 0:
            res.append(track)
            return
        for i in range(len(choice)):
            # choose
            tmp = choice[i]
            track += tmp
            # choice = choice[:i] + choice[i+1:]
            # next decision
            self.backtrack(choice[:i] + choice[i+1:], track, res)
            #unchoose
            track  = track[:-1]
            # choice = choice[:i] + tmp + choice[i+1:]



if __name__ == '__main__':
    s = Solution()
    string = 'ab1'
    print(s.Permutation(string))
