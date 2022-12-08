def fact(n): 

    if n==0 or n==1: 

        return 1 

    res=1 

    for num in range(1,n+1): 

        res=res*num 

    return res 

x=5 

ans=fact(x) 

print("the fact is",ans) 