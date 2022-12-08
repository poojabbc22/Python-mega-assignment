n=int(input("enter the number of people")) 

for n in range(1,n): 

        principal_amount=int(input("enter the amount")) 

        rate_interest=float(input("enter the rate of interest")) 

        time=int(input("enter the time period")) 

        simple_interest=(principal_amount*rate_interest*time)/100 

print("the simple interest is",simple_interest , "%") 