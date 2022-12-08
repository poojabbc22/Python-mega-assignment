def swap_two(list,pos1,pos2):
    get=list[pos1],list[pos2]
    list[pos2],list[pos1]=get
    return list
my_list=[23,45,99,12]
pos1,pos2=1,3
print(swap_two(my_list,pos1-1,pos2-1))