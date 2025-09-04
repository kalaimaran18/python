# HCF and GCD program using python Code.

def hcf(a,b):
    small=min(a,b)

    for i in range(1,small+1):
        if a%i==0 and b%i==0:

            hcf_value=i
    return hcf_value

num1=60
num2=48

print(hcf(num1,num2))