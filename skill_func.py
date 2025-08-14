'''
Though Python passes by reference, the below program will still print 100 200 300,
as in the called function, the variable items is assigned a new list containing the values 800, 900, 1000
Hence the values in the list numbers remain unchanged.

 '''


# Example Program using Functions

def modifyvalues(items):
    items [800, 900, 1000]

    numbers=[100,200,300]

    modifyvalues (numbers)

    for num in numbers:

        print(num,end="")

# Example Program using Functions

def changevalues(marks):

    marks[0]=40
    mark=[1,2,3]

    marks[0] = 50
    marks[1] = 60
    marks[2] = 70

studentmarks = [10, 50, 60]
changevalues(studentmarks) 
for min in studentmarks:
    print(studentmarks,end=" ")