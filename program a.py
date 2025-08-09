# multiple number divisible till X

n=int(input())
x=int(input())

num=n

while num%x!=0:

    print(num,end=" ")

    num=num+n

print(num)


#largest number in given input

n=int(input())
large=0

for i in range(n):

    z=int(input())

    if z>large:
        large=z
print(large)

    