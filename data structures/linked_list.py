class Node:
    def __init__(self , value = None):
        self.value = value
        self.next = None
        
class LinkedList: # use singly LinkedList
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self): #for linkedlist iterrations
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self , value , index = -1): #for insert value
        startNode = None 
        endNode = None

        if type(value).__name__ == "list":
            previousNode = Node(value[0])
            startNode = previousNode
            
            for i in range(1 , len(value)):
                currentNode = Node(value[i])
                previousNode.next = currentNode
                previousNode = currentNode

            endNode = previousNode
        else:
            startNode = Node(value)
            endNode = startNode

        if self.head is None:
            self.head = startNode
            self.tail = endNode
        elif index == 0:
            endNode.next = self.head
            self.head = startNode
        elif index == -1:
            self.tail.next = startNode
            self.tail = endNode
        else:
            tempNode = self.head
            i = 0
            while i < index - 1:
                tempNode = tempNode.next
                i += 1
            endNode.next = tempNode.next
            tempNode.next = startNode

    def search(self , value): # search element available or not
        if self.head is None:
            return False
        else:
            node = self.head
            while node is not None:
                if value == node.value:
                    return True
                node = node.next
            else:
                return False

    def delete(self, index = -1): #delete element using index
        if index == 0:
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif index == -1:
            node = self.head
            while node is not None:
                if node.next == self.tail:
                    break
                node = node.next
            node.next = None
            self.tail = node
        else:
            tempNode = self.head
            i = 0
            while i < index - 1:
                tempNode = tempNode.next
                i += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next


# Demonstration

def printList(linkedList): # helping loop for print LinkedList
    for node in linkedlist:
        print(node.value , end= " ")
    print()

linkedlist = LinkedList() # create LinkedList
node1 = Node(5) # create Node 1
node2 = Node(10) # create Node 2
linkedlist.head = node1 # create link between head and node 1
node1.next = node2 # create link between node 1 and node 2
linkedlist.tail = node2 # create link between node 2 and tail
printList(linkedlist) # print updated LinkedList

linkedlist.insert([6 , 7 , 8 , 9],1) # insert method 
printList(linkedlist) # print updated LinkedList

print(linkedlist.search(5)) # print given element exist or not in LinkedList

linkedlist.delete(2) # delete element in LinkedList using index
printList(linkedlist) # print updated LinkedList