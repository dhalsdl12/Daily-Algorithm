class MyQueue:

    def __init__(self):
        self.queue = []
        return None

    def push(self, x: int) -> None:
        self.queue.append(x)
        return None

    def pop(self) -> int:
        ans = self.queue[0]
        self.queue = self.queue[1:]
        return ans

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()