from typing import List, Tuple
def twoSum(array:List[int], target: int  ) -> List[int]:
    """
    sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    # A dictionary to store each number and it indexex
    num_index = { }

    # looping through the arrays to get each number and it' index 

    for index, number in enumerate(array):
        
        difference = target - number

        # check for the particular number in the hashed map to store

       