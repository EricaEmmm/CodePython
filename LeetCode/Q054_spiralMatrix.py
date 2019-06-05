# 螺旋矩阵
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# 示例 1:
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#
# 示例 2:
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
	#法一：
	#取首行，去除首行后，对矩阵转置来创建新的矩阵，
    #再递归直到新矩阵为[],退出并将取到的数据返回
	def spiralOrder1(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		res = []
		if matrix == []:
			return res
		res.extend(matrix[0])							#取首行
		new = [reversed(i) for i in matrix[1:]]			#返回一个反转的迭代器
		tmp = self.spiralOrder([i for i in zip(*new)])	#对转置矩阵递归
		res.extend(tmp)
		return res
	# 法二：超时！！
	def spiralOrder2(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		res = []
		if matrix == []:
			return res
		row, col, dr, dc  = len(matrix)-1, len(matrix[0])-1, 0, 0
		cnt = (row+1) * (col+1)

		while cnt:
			for i in range(dc, col-dc):			#上
				#if cnt > 0:
					res.append(matrix[dr][i])
					cnt -= 1
			for i in range(dr, row-dr):			#右
				#if cnt > 0:
					res.append(matrix[i][col-dc])
					cnt -= 1
			for i in range(col-dc, dc, -1):		#下
				#if cnt > 0:
					res.append(matrix[row-dr][i])
					cnt -= 1
			for i in range(row-dr, dr, -1):		#左
				#if cnt > 0:
					res.append(matrix[i][dc])
					cnt -= 1
			dr += 1
			dc += 1
		return res
	# 法三：
	def spiralOrder3(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		res = []
		if matrix == []:
			return res
		row, col  = len(matrix), len(matrix[0])
		cnt = (min(row, col) + 1) // 2

		for c in range(cnt):
			for i in range(c, col-c):			#上
				res.append(matrix[c][i])
			for i in range(c+1, row-c-1):		#右
				res.append(matrix[i][col-c-1])
			for i in range(col-c-1, c, -1):		#下
				res.append(matrix[row-c-1][i])
			for i in range(row-c-1, c, -1):		#左
				res.append(matrix[i][c])
		return res[:row*col]	#截断，因为当单行或单列时候，右下左上会造成重复读取

	def spiralOrder(self, matrix):
		return self.spiralOrder3(matrix)


if __name__ == '__main__':
	matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
	s = Solution()
	# t=[1, 2, 3, 4]
	# print(t[:4])
	print(s.spiralOrder(matrix))
	#print((3)//2)
	# res=[]
	# res.append(1)
	# print(res)
	# aList = [123, 'xyz', 'zara', 'abc', 123];
	# bList = [2009, 'manni'];
	# aList.extend(bList)  # 列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
	# print(aList)
	# print(bList)
	# t = [[5, 6, 7, 8],
	# 	[9, 10, 11, 12]
	# ]#[reversed(i) for i in matrix[1:]]
	# p = [i for i in zip(*t)]
	# # print(t)
	# print(p)