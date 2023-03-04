# For the product just multiply up to n-times, but start with n=6, so 2(*2*2*2*2*2*2) = 256 up to n-times
# In other words, how many times do I have to multiply 2 by 2 with when n=6? well 6
class Product:
    @staticmethod
    def iterative(n: int) -> int:
        result: int = 2 ** n
        return result 
    
   

    @staticmethod
    def recursive(n: int) -> int:
        if n == 0: # because x**0 is 1  # base case
            return 1
        else:
        #    return 2 * power_of_two(n -1)
            return 2 * Product.recursive(n -1)
        
         
    """ def power_of_two(n: int) -> int:
        result = 1
        for i in range(n):
            result *= 2
        return result """
        
    


# Test case(s):
n: int = 6
result: int = Product.iterative(n)
assert result == 64, f"got {result}, expected 64"

result = Product.recursive(n)
assert result == 64, f"got {result}, expected 64"


