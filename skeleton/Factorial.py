# For the factorial just do for n, so for n = 5, 5! = 120
class Factorial:
    @staticmethod
    def iterative(n: int) -> int:
        raise NotImplementedError("Please implement me!")

    @staticmethod
    def recursive(n: int) -> int:
        raise NotImplementedError("Please implement me!")


# Test case(s):
n: int = 5
result: int = Factorial.iterative(n)
assert result == 120, f"got {result}, expected 120"

result = Factorial.recursive(n)
assert result == 120, f"got {result}, expected 120"
