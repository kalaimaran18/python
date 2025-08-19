'''
#A string value containing more than one word is passed as the input to the program. 
# Toggle the case of the letters only in the first word.

Example Input/Output:

Input:

This is my HOME

Output:

THIS is my HOME

'''
strval=input()
words=strval.split()
print(words[0].swapcase(),end=" ")
for w in words [1::]:
    print(w, end=" ")



'''
Certain space separated numbers are passed as the input to the program. 
The program must print only the even numbers in the reverse order of their occurrence in the input sequence.

Input:

10 99 23 12 78 81 102

Output:

102 78 12 10

'''
var=list(map(int,input().split(" ")))

for i in var[::-1]:

    if i%2==0:
        print(i,end=" ")