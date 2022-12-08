def swap_list(my_list):
    size=len(my_list)
    temp=my_list[0]
    my_list[0]=my_list[size-1]
    my_list[size-1]=temp
    return my_list
my_list=[1,3,8,5,9]
print(swap_list(my_list))
