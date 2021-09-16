"""Given the array candies and the integer extraCandies, where candies[i] 
represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the 
kids such that he or she can have the greatest number of candies among them. 
Notice that multiple kids can have the greatest number of candies.

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true].

Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy, therefore only kid 1 will have 
the greatest number of candies among the kids regardless of who takes the extra candy."""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # make empty list 
        result = []
        
        #iterate in list candies 
        for candy in candies:
            
            # check if candies + extraCandies is bigger or the same size as the maximum in candies
            if candy + extraCandies >= max(candies):
                # if true add True to list result
                result.append(True)
                
            else: 
                # if false add False to list result
                result.append(False)
        # return list       
        return result
                    

                    
                
