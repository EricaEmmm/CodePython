'''
车辆时刻表分组
某车站为了方便管理，决定根据目的地以及出发时间的不同对车辆时刻表进行分组管理。
要求：给定一个时刻表，同一个目的地的车辆必须分配在同一组内，分组不能打乱时刻表的车次顺序，
即各个分组之间出发时间有序。请对时刻表尽可能多的分组，按出发时间早晚作为输出顺序。
输入
时刻表内容：aabbcddc，a,b,c,d为目的地，字母出现的先后顺序为出发时间的先后顺序
输出
输出各个分组的长度，以空格相隔，输出顺序与时刻表的出发顺序一致
样例
输入：aabbcddc
输出：2,2,4
提示：aabbcddc 可分为aa,bb,cddc三组，目的地相同的车辆分配在了一组，同时，aa分组出发时间早于bb分组，
bb分组早于cddc分组，所以输出结果为2，2，4。若分为一组，aabbcddc，则不满足题目中尽可能多的分组这一要求。
输入不为空
'''

from collections import Counter

def helper(dic, target):
    flag = 0
    tmp = 0
    for k, v in dic.items():
        tmp += v
        if target[k] != 0:
            flag = 1
    return flag, tmp

if __name__ == '__main__':
    targets = 'abab'    #input()   #
    if len(targets) < 2:
        print(len(targets))

    target = Counter(targets)
    res = []
    dic = {}
    for x in targets:
        if dic == {}:
            dic[x] = 1
            target[x] -= 1
            flag, tmp = helper(dic, target)
            if flag == 0:
                res.append(tmp)
                dic = {}
        else:
            dic[x] = dic.get(x, 0) + 1
            target[x] -= 1
            flag, tmp = helper(dic, target)
            if flag == 0:
                res.append(tmp)
                dic = {}
    print(','.join(map(str, res)))