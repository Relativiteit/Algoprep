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
        print(n)
        if n <= 1:
            return 1
        else:
            return sum(Summation.recursive(n-1))


# Test case(s):
n: int = 10
result: int = Summation.iterative(n)
assert result == 10, f"got {result}, expected 10"

result = Summation.recursive(n)
assert result == 10, f"got {result}, expected 10"
