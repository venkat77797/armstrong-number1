def arm_strong(n,res=0):
    l=len(str(n))
    n1=n
    while n:
        r=n%10
        n=n//10
        res+=r**l
    if(res==n1):
        print("Armstrong number")
    else:
        print("Not an armstrong number")
    


n=int(input())
arm_strong(n)


























