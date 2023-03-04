# For the summation just count up till n, so increment by 1, so 1+1+1+1...+1 <=n
class Summation:
    @staticmethod
    def iterative(n: int) -> int:
        counter: int = 0 
        for i in range(n):
            counter += 1 

        return counter  

    @staticmethod
    def recursive(n: int) -> int:
        if n == 0:  # base case if n is 0 don't count
            return n 
        else:
            return n +  Summation.recursive(n - 1)
    


# Test case(s):
n: int = 10
result: int = Summation.iterative(n)
assert result == 10, f"got {result}, expected 10"

result = Summation.recursive(n)
assert result == 55, f"got {result}, expected 10"
