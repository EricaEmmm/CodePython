'''
挖矿游戏
1.每次可挖多个矿石，每个矿石重量不一样，需要用平衡车运下山；
2.平衡车有左右两个车厢，必须保证两个车厢重量完全相等，且矿石数量相差不超过1个，才能运下山。
小v挖到n（<100）个矿石，每个重量不超过100。保证一次性将n个矿石运出去，可以购买配重砝码。最少要买多少重量砝码。
输入：3 7 4 11 8 10
输出：1
说明：将3,7,11放左车厢，4,8,10放右车厢，买重量1的砝码放左车厢
'''

def solution(stone_list):
    stone_list = sorted(stone_list)
    if len(stone_list) % 2 == 1:
        stone_list.append(0)
    res = 0
    i = 0
    while i < len(stone_list):
        tmp = abs(stone_list[i] - stone_list[i+1])
        res = min(abs(res+tmp), abs(res-tmp))
        i += 2
    return abs(res)
    pass

stone_list = [3, 7, 4, 11, 8, 10]   #[1,2,3,4,100]    #[int(i) for i in input().split()]
print(solution(stone_list))