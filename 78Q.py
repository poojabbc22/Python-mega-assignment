def compound_interest(principal,rate,time): 

       Amount=principal*(pow((1+rate/100),time)) 

       compount=Amount-principal 

       print("compouund interest is",compount) 

compound_interest(1000,23,4) 