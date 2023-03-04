# For the remainder just return back what the remainder is of a given n, 
# and a given m, so n % m, if n = 5, and m = 2, the remainder is 1
class Mod:
    @staticmethod
    def iterative(
        n: int, # Dividend so n % m, if n = 5, and m = 2, the remainder is 1
        m: int, # Divisor
    ) -> int:
        remainder: int = n % m 
        return remainder

    @staticmethod
    def recursive(
        n: int, # Dividend
        m: int, # Divisor
    ) -> int:
        if n == m: # base case if n == m return 0 
            return 0
        elif n < m:
            return n 
        elif m == 0:
            raise ValueError('Cant divide by zero')
        else: 
            remainder = Mod.recursive(n-m, m)
            return remainder 

# Test case(s):
n: int = 5
m: int = 2
result: int = Mod.iterative(n, m)
assert result == 1, f"got {result}, expected 1"

result = Mod.recursive(n, m)
assert result == 1, f"got {result}, expected 1"

n = 25
m = 7
result = Mod.iterative(n, m)
assert result == 4, f"got {result}, expected 4"

result = Mod.recursive(n, m)
assert result == 4, f"got {result}, expected 4"

n = 25677
m = 44
result: int = Mod.iterative(n, m)
assert result == 25, f"got {result}, expected 25"

result = Mod.recursive(n, m)
assert result == 25, f"got {result}, expected 25"
