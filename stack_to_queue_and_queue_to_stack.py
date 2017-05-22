from linkedstack import LinkedStack
from linkedqueue import LinkedQueue
from copy import deepcopy


def stack_to_queue(my_stack):
    s = deepcopy(my_stack)
    q = LinkedQueue()
    while not s.isEmpty():
        q.add(s.peek())
        s.pop()
    return q


def queue_to_stack(my_queue):
    q = deepcopy(my_queue)
    s = LinkedStack()
    while not q.isEmpty():
        s.add(q.peek())
        q.pop()
    return s


ss = LinkedStack()

for i in "randomletters":
    ss.push(i)
qq = stack_to_queue(ss)
for i in qq:
    print(i, end='')
print("\n")
ss = queue_to_stack(qq)
for i in ss:
    print(i, end='')
