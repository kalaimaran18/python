'''
The age of a person is passed as the input. The program must print the output based on the value of the age as given below.
If the value of age is from 1 to 12, the output must be Child.
If the value of age is from 13 to 19, the output must be Teen.
If the value of age is 20 or more, the output must be Adult.

'''
age=int(input())
if age<=12:
    print("Child")
elif age<=19:
    print("Teen")
else:
    print("Adult")


#Fill in the missing lines so that the program prints the input value N without modification when N is a multiple of 5. 
# Else the program prints N+10 as the output.

N=int(input())
if N%5==1:
    print(N+10)
else:
    print(N)