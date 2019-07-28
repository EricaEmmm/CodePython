# 回合制游戏
# 你在玩一个回合制角色扮演的游戏。现在你在准备一个策略，以便在最短的回合内击败敌方角色。在战斗开始时，敌人拥有HP格血量。
# 当血量小于等于0时，敌人死去。一个缺乏经验的玩家可能简单地尝试每个回合都攻击。但是你知道辅助技能的重要性。
# 在你的每个回合开始时你可以选择以下两个动作之一：聚力或者攻击。
#     聚力会提高你下个回合攻击的伤害。
#     攻击会对敌人造成一定量的伤害。如果你上个回合使用了聚力，那这次攻击会对敌人造成buffedAttack点伤害。否则，会造成normalAttack点伤害。
# 给出血量HP和不同攻击的伤害，buffedAttack和normalAttack，返回你能杀死敌人的最小回合数。
#
# 输入描述:
# 第一行是一个数字HP
# 第二行是一个数字normalAttack
# 第三行是一个数字buffedAttack
# 1 <= HP,buffedAttack,normalAttack <= 10^9
# 输出描述:
# 输出一个数字表示最小回合数
#
# 输入例子1:
# 13
# 3
# 5
# 输出例子1:
# 5


# buff=0，表示上个回合攻击了，这个回合只能normalAttack
# buff=1，表示上个回合聚力了，这个回合只能normalAttack
def helper(HP, normalAttack, buffedAttack, buff):
    if HP <= 0:
        return
    if buff:
        return min(helper(HP-normalAttack), normalAttack, buffedAttack, 1)



if __name__ == '__main__':
    HP = int(input())
    normalAttack = int(input())
    buffedAttack = int(input())

    if normalAttack >= HP:
        print(1)

    res = 0
    if normalAttack * 2 >= buffedAttack:    # 当蓄力的伤害不高于普通伤害的二倍的时候，全用普通伤害
        # while HP > 0:
        #     res += 1
        #     HP -= normalAttack
        # print(res)
        res = HP // normalAttack
        if HP-res*normalAttack > 0:
            print(res+1)
        else:
            print(res)
    else:
        # while HP > normalAttack:
        #     res += 2
        #     HP -= buffedAttack
        # if HP <= 0:
        #     print(res)
        # else:
        #     print(res+1)
        res = HP // buffedAttack
        if HP-res*buffedAttack > normalAttack:
            print(2*(res+1))
        elif HP-res*buffedAttack > 0:
            print(2*res+1)
        else:
            print(2*res)



