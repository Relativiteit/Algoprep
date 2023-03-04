# For the factorial just do for n, so for n = 5, 5! = 120
class Factorial:
    @staticmethod
    def iterative(n: int) -> int:
        if n < 0:
            raise ValueError('Factorial does not work for negative numbers')
        elif n == 0:
            return 1
        else:
            result: int = 1 
            for i in range(1, n + 1):
                result *= i  
            return result 
           
    @staticmethod
    def recursive(n: int) -> int:
        if n == 0: # base case factorial 0 is 1 
            return 1
        elif n < 0: 
            raise ValueError('Factorial does not work for negative numbers')
        else: 
            return n * Factorial.recursive(n -1 )
        


# Test case(s):
n: int = 5
result: int = Factorial.iterative(n)
assert result == 120, f"got {result}, expected 120"

result = Factorial.recursive(n)
assert result == 120, f"got {result}, expected 120"
