n=int(input("enter  the number")) 

def arm_check(n): 

    if n in range(1,10): 

        return True 

    length=len(str(n)) 

    sum=0 

    original=n 

    while(n>0): 

        digit=n % 10 

        sum +=digit **length 

        n=n//10 

    if sum==original: 

        return True 

    else: 

        return False 

arm_check(n) 
 

if arm_check(n): 

    print(n,"is armstrong") 

else: 

    print(n,"is nott")