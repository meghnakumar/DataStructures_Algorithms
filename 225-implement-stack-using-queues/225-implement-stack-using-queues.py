from collections import deque
class MyStack(object):

    def __init__(self):
        self.queue = deque()
        
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.appendleft(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]
        
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()