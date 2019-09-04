'''
AUC计算
ROC-AUC是一种常用的模型评价指标，它是ROC曲线下的面积。现在已知样本数据集的真实值(1为正样本，0为负样本)
和某二分类器在该样本数据集上的预测值（属于正样本的概率，且各不相同），求ROC-AUC，精确到小数点后两位。
输入
第1行为训练样本的数量N。
第2到N+1行的每行为样本的实际类别与预测值，以空格分隔。
输出
计算ROC-AUC，精确到小数点后两位。
样例输入
10
1 0.90
0 0.70
1 0.60
1 0.55
0 0.52
1 0.40
0 0.38
0 0.35
1 0.31
0 0.10
样例输出
0.68
提示
可以按定义计算，也可以计算随机挑选一对正负样本，正样本的预测值大于负样本的预测值的概率。
'''

def auc(labels, preds):
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    total_pair = n_pos * n_neg

    labels_preds = zip(labels, preds)
    labels_preds = sorted(labels_preds, key=lambda x: x[1])
    accumulated_neg = 0
    satisfied_pair = 0
    for i in range(len(labels_preds)):
        if labels_preds[i][0] == 1:
            satisfied_pair += accumulated_neg
        else:
            accumulated_neg += 1

    return satisfied_pair / float(total_pair)

if __name__ == "__main__":
    n = int(input())
    labels = []
    preds = []
    for i in range(n):
        label, pred = list(map(float, input().split()))
        labels.append(label)
        preds.append(pred)
    print(auc(labels, preds))