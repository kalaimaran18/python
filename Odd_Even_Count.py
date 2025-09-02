# Count of 1 to 10 range odd and even numbers.

odd_count=0
even_count=0

for i in range(1,11):
    if i%2==1:
        odd_count=odd_count+1
    
    else:
        even_count=even_count+1

print(odd_count)
print(even_count)