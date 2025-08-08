#Identify the colour code

c=input()

if c=='r' or c=='R':
    print("RED")

elif c=='g' or c=='G':
    print("GREEN")
elif c=='b' or c=='B':
    print("BLUE")
else:
    print("UNDEFINED")



#Using python for solve (n is not divisible of a,b)


a=int(input())   # 1
b=int(input())   # 10
n=int(input())   # 3

for i in range(a,b+1):
    if i%n !=0:
        print(i,end=" ")  #output(1,2,4,5,7,8,10)
