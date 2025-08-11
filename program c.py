#Question 

'''A polygon is with N sides. The program must accept the length of the N sides and print the perimeter P of the polygon as the output.

Input Format:

The first line denotes the value of N.
Next N lines contain the length of the N sides.

Output Format:

The first line contains the the perimeter P of the polygon

Boundary Conditions:

3<= N <= 100

The length of the side is an integer value from 1 to 999999.

Example Input/Output 1:

Input:
3
100
60
70

Output

230

'''
# Answer of the problem


N=int(input())
s=0
for i in range(N): 
    v=int(input())
    s+=v
print(s)
