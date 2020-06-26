class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def reverseListIteratively(self, head):
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def reverseListRecursively(self, head):
        current = head
        if current == None or current.next == None:
            return current
        p = self.reverseListRecursively(current.next)
        current.next.next = current
        current.next = None
        return p
