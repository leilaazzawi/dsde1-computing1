# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    x = the_list[index]
    new_list = the_list.insert(index, x)
    print(new_list)
    return(new_list)

repeat_at_index([1,2,3], 2)