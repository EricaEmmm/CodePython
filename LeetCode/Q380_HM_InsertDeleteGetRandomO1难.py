# 常数时间插入、删除和获取随机元素
# 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
#     insert(val)：当元素 val 不存在时，向集合中插入该项。
#     remove(val)：元素 val 存在时，从集合中移除该项。
#     getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
#
# 示例 :
# // 初始化一个空的集合。
# RandomizedSet randomSet = new RandomizedSet();
#
# // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomSet.insert(1);
#
# // 返回 false ，表示集合中不存在 2 。
# randomSet.remove(2);
#
# // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomSet.insert(2);
#
# // getRandom 应随机返回 1 或 2 。
# randomSet.getRandom();
#
# // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomSet.remove(1);
#
# // 2 已在集合中，所以返回 false 。
# randomSet.insert(2);
#
# // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
# randomSet.getRandom();

import random

# 法一：时间不是O(1)
class RandomizedSet1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            self.map[val] = 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            del self.map[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        index = random.randint(0,len(self.map)-1)
        return [k for k in self.map.keys()][index]

# 法二：用两个哈希表
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_index = {} #记录键、下标对
        self.index_key = {} #记录下标、键对
        self.len = 0        #记录长度，便于随机返回元素

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # 插入时，分别对两个哈希表都进行插入，同时len+1
        if val not in self.key_index.keys():
            self.len += 1
            self.key_index[val] = self.len
            self.index_key[self.len] = val
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.key_index.keys():
            self.index_key[self.key_index[val]] = self.index_key[self.len]      # 将index_key中键为len的覆盖到键为key_index[val]，然后删除键为len的
            self.key_index[self.index_key[self.len]] = self.key_index[val]      # 将key_index中键为val的覆盖到键为index_key[len]，然后删除键为val的
            del self.index_key[self.len]    # 删除最后的键值对
            del self.key_index[val]         # 删除val
            self.len -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.index_key[random.randint(1,self.len)]

if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.insert(1))
    print(obj.insert(2))
    print(obj.insert(3))
    print(obj.remove(2))
    print(obj.remove(2))
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())