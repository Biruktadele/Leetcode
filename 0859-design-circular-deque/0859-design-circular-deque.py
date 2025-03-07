class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.pre = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.k = k
        self.head = None
        self.til = None

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            node = Node(value)
            if not self.head or not self.til:
                self.head = node
                self.til = node
            else:
                node.next = self.head
                self.head.pre = node
                self.head = node
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            node = Node(value)
            if not self.head or not self.til:
                self.head = node
                self.til = node
            else:
                node.pre = self.til
                self.til.next = node
                self.til = node
            self.size += 1
            return True
        return False
        

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.head = self.head.next
            
            if not self.head:
                self.til = None
            else:
                self.head.pre = None
            self.size -= 1
            return True
        return False
        
    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.til = self.til.pre
            if not self.til:
                self.head = None
            else:
                self.til.next = None
            self.size -= 1
            return True
        return False
        
    def getFront(self) -> int:
        if self.size:
            return self.head.val
        return -1
    def getRear(self) -> int:
        if self.size:
            return self.til.val
        return -1
    def isEmpty(self) -> bool:
        return self.size == 0
    def isFull(self) -> bool:
        return self.size >= self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()