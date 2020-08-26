#https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.queue:
            return False
        return True

    def print_queue(self) :
        print(self.queue)

if __name__ == '__main__':

    queue = MyQueue()

    queue.push(1)
    queue.push(2)
    queue.print_queue()
    queue.peek()
    queue.pop()
    queue.empty()
    queue.print_queue()