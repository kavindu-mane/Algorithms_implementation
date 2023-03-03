class BSTNode:
    def __init__(self , data = None):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def insertNode(nodeValue , rootNode):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue < rootNode.data:
        if rootNode.leftNode is None:
            rootNode.leftNode = BSTNode(nodeValue)
        else:
            insertNode(nodeValue , rootNode.leftNode)
    elif nodeValue > rootNode.data:
        if rootNode.rightNode is None:
            rootNode.rightNode = BSTNode(nodeValue)
        else:
            insertNode(nodeValue , rootNode.rightNode)

def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data , end= " ")
    preOrder(rootNode.leftNode)
    preOrder(rootNode.rightNode)

def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftNode)
    print(rootNode.data , end= " ")
    inOrder(rootNode.rightNode)

def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.leftNode)
    postOrder(rootNode.rightNode)
    print(rootNode.data , end= " ")

def search(rootNode , searchData):
    if rootNode.data == searchData:
        return True
    elif rootNode.data > searchData:
        if rootNode.leftNode is not None:
            if(rootNode.leftNode.data == searchData):
                return True
            else:
                return search(rootNode.leftNode ,  searchData)
        else:
            return False
    elif rootNode.data < searchData:
        if rootNode.rightNode is not None:
            if(rootNode.rightNode.data == searchData):
                return True
            else:
                return search(rootNode.rightNode ,  searchData)
        else:
            return False

def delete(rootNode ,  deleteData):
    if rootNode is None:
        return rootNode
    if rootNode.data > deleteData:
        rootNode.leftNode = delete(rootNode.leftNode , deleteData)
    elif rootNode.data < deleteData:
        rootNode.rightNode  = delete(rootNode.rightNode , deleteData)
    else:
        if rootNode.leftNode is None:
            temp = rootNode.rightNode
            rootNode = None
            return temp
        elif rootNode.rightNode is None:
            temp = rootNode.leftNode
            rootNode = None
            return temp
        else:
            current = rootNode.rightNode
            while current.leftNode is not None:
                current = current.leftNode
            rootNode .data = current.data
            rootNode.rightNode = delete(rootNode.rightNode , current.data)
    return rootNode


# Demonstration
def helpingFunction(rootNode):
    print("Pre-Order Traversal \t= " , end= " ")
    preOrder(rootNode)
    print("\nIn-Order Traversal \t= " , end= " ")
    inOrder(rootNode)
    print("\nPost-Order Traversal \t= " , end= " ")
    postOrder(rootNode)
    print()

rootNode = BSTNode(6)
insertNode(4 , rootNode)
insertNode(8 , rootNode)
insertNode(2 , rootNode)
insertNode(5 , rootNode)
insertNode(9 , rootNode)
insertNode(1 , rootNode)
helpingFunction(rootNode)

print(search(rootNode , 10))

delete(rootNode , 4)
helpingFunction(rootNode)

