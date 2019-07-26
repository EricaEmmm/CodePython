# 给定一个版本号数组['4.1', '4.7.1', '4.8', '4.8.0', '4.10', '5'] ，按照规则进行排序
# 1、'4.8'要排在'4.8.0'前面
# 2、'4.1'要排在'4.10'前面


def versionSort(versions):
    """
    使用选择排序
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    :param versions: list
    :return:
    # ver = []
    # for i in range(n):
    #     ver.append(list(map(int, versions[i].split('.'))))
    """
    n = len(versions)
    ver = list(map(lambda x:list(map(int, x[1:].split('.'))), versions))

    for i in range(n):
        # 选定首位为最小值:
        minIndex = i
        # 找到最小值下标
        for j in range(i, n):
            min = 0
            cur = 0
            for k in range(len(ver[j])):
                if len(ver[minIndex]) < k + 1:
                    break
                min += ver[minIndex][k]
                cur += ver[j][k]
                if min > cur:
                    minIndex = j
                if min < cur:
                    break
        # 交换
        if minIndex > i:
            versions[i], versions[minIndex] = versions[minIndex], versions[i]
    return versions



if __name__ == '__main__':
    versions = ['v4.1', 'v4.7.1', 'v1', 'v4.8', 'v4.8.0', 'v4.10', 'v5'] #['1.0.2', '1.0.21', '1.2.11', '2.0.1', '2.2.9']#
    # ver = list(map(lambda x: list(map(int, x.split('.'))), versions))
    # print(ver)
    print(versionSort(versions))