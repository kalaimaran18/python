
n=int(input())
x=int(input())
for i in range(n,x+2):
    print(i,end=" ")
    if n>i:
        print(i)
        
#number of values

number=set()
number.add(79)
number.add(60)
number.add(69)
number.add(70)
for num in number:
    print(num)

    
# appendleft() and popleft()

from collections import deque
x=int(input())
y=int(input())
z=int(input())

queue=deque()
queue.appendleft(x)       #appendleft is a defifnd first element of the input
queue.appendleft(y)
queue.appendleft(z)

print(queue.popleft(),end=" ")
print(queue.popleft(),end=" ")
print(queue.popleft(),end=" ")

#stack pop() method.

n=int(input())
r=int(input())
x=int(input())

stack=[n,r,x]
stack.append(23)
print(stack.pop(),end=" ")
stack.append(r)
print(stack.pop(),end=" ")
print(stack.pop(),end=" ")