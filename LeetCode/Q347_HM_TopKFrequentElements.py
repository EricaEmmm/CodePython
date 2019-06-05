# 前K个高频元素
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
# 示例 2:
# 输入: nums = [1], k = 1
# 输出: [1]
# 说明：
#     你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
#     你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
#

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1  # 返回指定键的值，如果值不在字典中返回default值
            # if i in map:
            #     map[i] += 1
            # else:
            #     map[i] = 1
        return [x[0] for x in sorted(map.items(), key = lambda item : item[1], reverse = True)][:k]
        # res = []
        # tmp = sorted(map.items(), key = lambda item : item[1], reverse = True)  # 返回值是一个list，而原字典中的键值对被转换为了list中的元组
        # for i in tmp[:k]:
        #     res.append(i[0])
        # return res


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2))

    # t = [('a',1), ('b',2), ('c',3)]
    # print(t[2][1])
