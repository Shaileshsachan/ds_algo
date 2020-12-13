########################## SORTING WITH STACK ###################
# def create_stack():
#     stack = []
#     return stack
#
#
# def isEmpty(stack):
#     return len(stack) == 0
#
#
# def push(stack, item):
#     stack.append(item)
#
#
# def top(stack):
#     p = len(stack)
#     return stack[p-1]
#
#
# def pop(stack):
#     if(isEmpty(stack)):
#         print("Stack Underflow")
#         exit(1)
#     return stack.pop()
#
#
# def prints(stack):
#     for i in range(len(stack)-1, -1, -1):
#         print(stack[i], end=' ')
#     print()
#
#
# def sort_stack(stack):
#     t_stack = create_stack()
#     while(isEmpty(stack) == False):
#         tmp = top(stack)
#         pop(stack)
#
#         while(isEmpty(t_stack) == False and int(top(t_stack)) > int(tmp)):
#             push(stack, top(t_stack))
#             pop(t_stack)
#
#         push(t_stack, tmp)
#     return t_stack
#
#
# stack = create_stack()
# push(stack, str(34))
# push(stack, str(3))
# push(stack, str(31))
# push(stack, str(98))
# push(stack, str(92))
# push(stack, str(23))
#
# prints(stack)
# print("Sorted array".center(30, '-'))
# sortedst = sort_stack(stack)
# print(sortedst)


######################### STACK IMPLEMENTATION(     LIST    ) #######################

# stack = []
#
# stack.append("a")
# stack.append("b")
# stack.append("c")
#
# print("Initial Stack")
# print(stack)
#
# print("\nElements poped from stack")
# for i in range(len(stack)):
#     print(stack.pop())
#
# print("\nStack after elements are popped")
# print(stack)

#####################  IMPLEMENTATION USING COLLECTIONS.DEQUE  ################
#
# from collections import deque
#
# stack = deque()
#
# stack.append('a')
# stack.append('b')
# stack.append('c')
#
# print('Initial Stack')
# print(stack)
#
# print('\nElements poped from stack :')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
#
# print('\n Stack after elements are popped :')
# print(stack)

#############  IMPLEMENTATION USING QUEUE   ###########
#
# from queue import LifoQueue
#
# stack = LifoQueue(maxsize=4)
#
# print(stack.qsize())
#
# stack.put('a')
# stack.put('b')
# stack.put('c')
# stack.put('d')
#
# print("Full: ", stack.full())
# print("Size: ", stack.qsize())
#
# print('\nElements popped from the stack')
#
# for i in range(stack.qsize()):
#     print(stack.get())
#
# print('\nEmpty :', stack.empty())
# print('\nSize :', stack.qsize())
#


#################  IMPLEMENTATION USING SINGLY LINKED LIST  #########

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0


    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]


    def getSize(self):
        return self.size


    def isEmpty(self):
        return self.size == 0


    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value


    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1


    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from  an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")



























