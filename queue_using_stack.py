"""
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal 
queue (push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only 
push to top, peek/pop from top, size, and is empty operations are valid.

Depending on your language, the stack may not be supported natively. 
You may simulate a stack using a list or deque (double-ended queue) 
as long as you use only a stack's standard operations.

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

Constraints:
- 1 <= x <= 9
- At most 100 calls will be made to push, pop, peek, and empty.
- All the calls to pop and peek are valid.
"""

class MyQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []
        self.useA = True

    def push(self, x: int) -> None:
        if self.useA:
            self.stackA.append(x)
        else:
            self.stackB.append(x)

    def pop(self) -> int:
        if self.useA:
            while len(self.stackA) > 1:
                self.stackB.append(self.stackA.pop())
            self.useA = False
            return self.stackA.pop()
        else:
            while len(self.stackB) > 1:
                self.stackA.append(self.stackB.pop())
            self.useA = True
            return self.stackB.pop()

    def peek(self) -> int:
        if self.useA:
            while len(self.stackA) > 1:
                self.stackB.append(self.stackA.pop())
            self.useA = False
            ans = self.stackA.pop()
            self.stackB.append(ans)
            return ans
        else:
            while len(self.stackB) > 1:
                self.stackA.append(self.stackB.pop())
            self.useA = True
            ans = self.stackB.pop()
            self.stackA.append(ans)
            return ans

    def empty(self) -> bool:
        if len(self.stackA) == 0 and len(self.stackB) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.peek()
param_3 = obj.pop()
param_4 = obj.empty()

print(param_2)
print(param_3)
print(param_4)

print("Hello, World")
