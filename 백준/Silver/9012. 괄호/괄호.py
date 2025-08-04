# Node 클래스
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    # push
    def push(self, data):
        if self.top == None: 
            self.top = Node(data)  # 비어 있다면 새로운 노드를 만들어서 가리키게 하자
        else:
            curr = Node(data)    # 비어 있지 않다면 해당 data를 가진 Node를 만들고
            curr.next = self.top # 만들어진 노드의 next에 원래 top을 가리키게!!
            self.top = curr      # top을 방금 만들어진 node를 가리키게!!
    # pop
    def pop(self):
        if self.top == None:
            return None
        else:
            curr = self.top
            self.top = self.top.next
            return curr.data
    # peek
    def peek(self):
        if self.top == None:
            return None
        else:
            curr = self.top
            return curr.data
    # is_empty
    def is_empty(self):
        return self.top == None

T = int(input())
b_list = []
for i in range(T):
    b_list.append(input())

for test_case in b_list:
    b_stack = Stack()
    
    is_valid = True
    
    for b in test_case:
        if b == "(":
            b_stack.push(b)
        else:
            if b_stack.is_empty():
                is_valid = False
                break
            else:
                if b_stack.pop() == "(":
                    continue
                else:
                    is_valid = False
                    break
    
    if not b_stack.is_empty():
        is_valid = False
    
    print("YES" if is_valid else "NO")