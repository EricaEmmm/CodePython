# 选靓号
# A 国的手机号码由且仅由 N 位十进制数字(0-9)组成。一个手机号码中有至少 K 位数字相同则被定义为靓号。A 国的手机号可以有前导零，比如 000123456 是一个合法的手机号。
# 小多想花钱将自己的手机号码修改为一个靓号。修改号码中的一个数字需要花费的金额为新数字与旧数字之间的差值。比如将 1 修改为 6 或 6 修改为 1 都需要花 5 块钱。
# 给出小多现在的手机号码，问将其修改成一个靓号，最少需要多少钱？
#
# 输入描述:
# 第一行包含2个整数 N、K，分别表示手机号码数字个数以及靓号至少有 K 个数字相同。
# 第二行包含 N 个字符，每个字符都是一个数字('0'-'9')，数字之间没有任何其他空白符。表示小多的手机号码。
# 数据范围：
# 2 <= K <= N <= 10000
# 输出描述:
# 第一行包含一个整数，表示修改成一个靓号，最少需要的金额。
# 第二行包含 N 个数字字符，表示最少花费修改的新手机号。若有多个靓号花费都最少，则输出字典序最小的靓号。
#
# 输入例子1:
# 6 5
# 787585
# 输出例子1:
# 4
# 777577
# 说明:花费为4的方案有两种：777577与777775，前者字典序更小。

from collections import Counter

def get_cost(dct, aim_key, k):
    """
    :param dct:     电话号码数字 字典
    :param aim_key: 靓号数字
    :param k:       靓号数字出现次数
    :return:        最少花费cost
    """
    cost = 0
    k -= dct.get(aim_key, 0)
    if k <= 0:
        return cost
    for i in range(1, 10):
        # 比aim_key大i的数
        tmp_key = aim_key + i
        if tmp_key < 10:
            tmp_num = dct.get(tmp_key, 0)
            cost += i * min(tmp_num, k)
            k -= tmp_num
            if k <= 0:
                break
        # 比aim_key小i的数
        tmp_key = aim_key - i
        if tmp_key >= 0:
            tmp_num = dct.get(tmp_key, 0)
            cost += i * min(tmp_num, k)
            k -= tmp_num
            if k <= 0:
                break
    return cost

def modify(tel, aim_key, k):
    """
    :param tel:     电话号码
    :param aim_key: 靓号数字
    :param k:       靓号数字出现次数
    """
    if k <= 0:
        return
    for i in range(1, 10):
        # 比aim_key大i的数：要变化的值大于当前值，则从前往后替代
        tmp_key = aim_key + i
        if tmp_key < 10:
            for j in range(len(tel)):
                if tel[j] == tmp_key:
                    tel[j] = aim_key
                    k -= 1
                    if k <= 0: return
        # 比aim_key小i的数：要变化的值小于当前值，则从后往前替代
        tmp_key = aim_key - i
        if tmp_key >= 0:
            for j in range(len(tel)-1, -1, -1):
                if tel[j] == tmp_key:
                    tel[j] = aim_key
                    k -= 1
                    if k <= 0: return


if __name__ == "__main__":
    n, k = map(int, input().split())
    tel = [int(i) for i in input()]
    # 出现数字次数转化为字典
    # count_dct = {}
    # for i in tel:
    #     count_dct[i] = count_dct.get(i, 0) + 1
    count_dct = Counter(tel)

    # 先找到最少花费cost和靓号数字aim_key
    cost = float("inf") # 初始化代价为无穷大
    aim_key = None
    for i in range(0, 10):
        tmp = get_cost(count_dct, i, k)
        if tmp < cost and tmp >= 0:
            cost = tmp
            aim_key = i

    # 需要修改k个数字
    k -= count_dct.get(aim_key, 0)
    modify(tel, aim_key, k)

    print(cost)
    print(''.join(map(str, tel)))