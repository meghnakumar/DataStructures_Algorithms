class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        n = len(self.stack1) - 1
        for i in range(n):
            self.stack2.append(self.stack1.pop())
        popped = self.stack1.pop()
        for i in range(n):
            self.stack1.append(self.stack2.pop())
        return popped
        
        

    def peek(self):
        """
        :rtype: int
        """
        n = len(self.stack1) - 1
        for i in range(n):
            self.stack2.append(self.stack1.pop())
        popped = self.stack1[0]
        for i in range(n):
            self.stack1.append(self.stack2.pop())
        return popped
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1)==0 and len(self.stack2)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()