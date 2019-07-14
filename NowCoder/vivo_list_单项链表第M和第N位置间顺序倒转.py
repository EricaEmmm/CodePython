
class SNode:
    Next = None
    Value = None


def createLinkList(str):
    if len(str) <= 0:
        return None
    linkList = SNode()
    pNode = linkList

    for i in str:
        node = SNode()
        node.Value = i
        pNode.Next = node
        pNode = pNode.Next
    return linkList

def printLinkList(linkList):
    if linkList == None:
        print('None')
        return
    s = "head"
    node = linkList.Next
    while node != None:
        s = s + '->' + str(node.Value)
        node = node.Next
    print(s)

def reverseLinkList(linkList, m,n):
    preMNode = linkList
    for i in range(m-1):
        preMNode = preMNode.Next

    for i in range(n-m):
        preNNode = linkList
        for j in range(n-1):
            preNNode = preNNode.Next
        nNode = preNNode.Next
        preNNode.Next = preNNode.Next.Next
        nNode.Next = preMNode.Next
        preMNode.Next = nNode
        preMNode = preMNode.Next
    printLinkList(linkList)

if __name__ == "__main__":
    linkList = createLinkList([11,5,8,22,9,5,0])
    printLinkList(linkList)
    reverseLinkList(linkList,3,5)