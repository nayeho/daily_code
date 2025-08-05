class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front == None:
            curr = Node(data)
            self.front = curr
            self.rear = curr
        else:
            curr = Node(data)
            self.rear.next = curr
            self.rear = curr

    def dequeue(self):
        if self.front == None:
            return None
        else:
            curr = self.front
            self.front = self.front.next
            return curr.data

    def is_empty(self):
        return self.front == None
    
# 백준 2164번 카드2 문제
# 6 -> 4, 7 -> 6
N = int(input())

q = Queue()
# N이 6이라면 -> 1 ~ 6까지 Queue에 추가!!
for i in range(1, N + 1):
    q.enqueue(i)

while True:
    if q.front == q.rear: # q의 크기가 1
        break
    q.dequeue()

    if q.front == q.rear:
        break
    q.enqueue(q.dequeue())

# q의 크기는 1
print(q.dequeue())