from typing import List

def even_list(int_list: List[int]) -> List[int]:

    evenList = []
    for i in int_list:
        if i % 2 == 0:
            evenList.append(i)
    return evenList
    
    # TODO: Implement even_list
    pass
# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:

    
    
    
    
    
    
    # TODO: Implement sum_of_squares_of_even
    pass

# Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

# Boilerplate code
if __name__ == "__main__":
    main()