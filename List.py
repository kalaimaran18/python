# Python using List Operations.

a=[2,3,45,67,87,95,32,43]       #List 1
b=[12,13,90,93,21]              #List 2
print(type(a))
print(a)

a.pop()                         #automatically delete last value
print(a)

a.extend(b)                     # Merge two List 
print(a)

a.insert(0,6)                   # Insert New Element in List
a[6]=99

print(a)