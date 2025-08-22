'''
A number is passed as the input to the program. The program must print the output based on the conditions given below.
If the input number is odd and less than or equal to 1000, then the output must be double the number.

Your Program Output:
If the input number is odd and more than 1000 but less than or equal to 10000, 
then the output must be 200 less than the given number.
If the input number is odd and more than 10000, then the output must be 5000 less than the given number.
Else the input number is printed as such.

'''
i=int(input())

if i%2==1 and i<=1000:
    print(i*2)
elif i%2==1 and i<=10000:
    print(i-200)
elif i%2==1 and i>10000:
    print(i-5000)

else:
    print(i)

'''
A string S is passed as the input. Also a positive integer C is passed as the input. 
The program must print the characters in the string C times.

'''
S=input()
C=int(input())
for i in S:
    for S in range(C):
        print(i,end="")


#An integer value N is passed as the input. The program must print YES if N is prime number.
#Else the program must print NO.

n=int(input())
if n>1:
    for i in range(2,int(n**0.5 +1)):
        if n%i==0:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")