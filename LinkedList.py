class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def displayLinkedList(self):
        currentNode = self.head
        if(currentNode is None):
            print("LinkedList is empty")
            return
        while(currentNode):
            print(currentNode.data)
            currentNode = currentNode.next

    # adding node at end of linked list
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        currentNode = self.head
        while(currentNode.next):
            currentNode = currentNode.next
        currentNode.next = newNode

    # adding node at the beginning of linked list
    def prepend(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    # deleting node with data provided

    def deleteNode(self, data):
        currentNode = self.head
        # if the data we want to remove is the head Node of linked list
        if(cur_node and currentNode.data == data):
            self.head = currentNode.next
            return
        prevNode = None
        while(currentNode.data != data):
            prevNode = currentNode
            currentNode = currentNode.next
        prevNode.next = currentNode.next

    # deleting node with position provided
    def delNodePosition(self, position):
        currentNode = self.head
        if(position == 0):
            self.head = currentNode.next
            currentNode = None
            return
        count = 1
        prevNode = currentNode
        currentNode = currentNode.next
        while(currentNode and count != position):
            prevNode = currentNode
            currentNode = currentNode.next
            count += 1

        if currentNode is None:
            return
        prevNode.next = currentNode.next

    def lenCountIteratively(self):
        currentNode = self.head
        count = 0
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count

    def lenCountRecursive(self, node):
        if node is None:
            return 0
        else:
            return 1+self.lenCountRecursive(node.next)


a = LinkedList()
a.displayLinkedList()
a.append('A')
a.append('B')
a.prepend('C')
a.append('D')
a.displayLinkedList()
print(a.lenCountRecursive(a.head))
print("testing delete")
a.delNodePosition(3)
a.displayLinkedList()
