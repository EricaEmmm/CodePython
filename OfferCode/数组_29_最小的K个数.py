'''
最小的K个数
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''

'''
时间复杂度：O(nlogk)
空间复杂度：O(k)
'''
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return []
        import heapq
        bigheap = []
        for i in range(k):
            heapq.heappush(bigheap, -tinput[i])
        for j in range(k, len(tinput)):
            heapq.heappushpop(bigheap, -tinput[j])
        return sorted(map(lambda x:-x, bigheap))

if __name__ == '__main__':
    s = Solution()
    tinput = [4,5,1,6,2,7,3,8,9]
    print(s.GetLeastNumbers_Solution(tinput, 4))