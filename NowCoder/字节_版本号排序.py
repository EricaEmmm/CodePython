# 给定一个版本号数组['4.1', '4.7.1', '4.8', '4.8.0', '4.10', '5'] ，按照规则进行排序
# 1、'4.8'要排在'4.8.0'前面
# 2、'4.1'要排在'4.10'前面

def versionSort(versions):
    n = len(versions)
    ver = []
    for i in range(n):
        ver.append(map(int, versions[i].split('.')))
    return ver


if __name__ == '__main__':
    versions = ['4.1', '4.7.1', '4.8', '4.8.0', '4.10', '5']
    print(versionSort(versions))