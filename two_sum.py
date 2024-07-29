from typing import List, Tuple

def twoSum(array:List[int], target: int  ) -> List[int]:
    """
    Finds two indices of the two numbers such 
    that they add up to target.
    
    Args
    array(int): A list of integers
    target(int): The sum to find
    
    Return: 
    Indices of the number that adds up to the sum
    """
    # A dictionary to store each number and it indexex
    num_index = { }

    # looping through the arrays to get each number and it' index 

    for index, number in enumerate(array):
        
        difference = target - number
        # check for the particular number in the hashed map to store
        if difference in num_index:
            return [num_index[difference], index]

        num_index[number] = index
    return []
