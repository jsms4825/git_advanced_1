from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:

    evenList = []
    for i in int_list:
        if i%2 == 0:
            evenList.append(i)
            
    return evenList
    
    # TODO: Implement even_list
    pass