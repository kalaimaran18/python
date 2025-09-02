# Divisible by 3 and 5 with in range 1 to 100

count_3=0
count_5=0

for i in range(1,100+1):
    if i%3==0:
        count_3=count_3+1
        
    if i%5==0:
        count_5=count_5+1

print(count_3)
print(count_5)