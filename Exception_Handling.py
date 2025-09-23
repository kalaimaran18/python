# Exception Handling 
# Example 

try:
    a=int(input())
    b=int(input())
    print(a/b)

except TypeError as e:
    print("Type",e)
except ValueError as e:
    print("value",e)
except Exception:
    print("something Wrong")

finally:
    print("DOne")

