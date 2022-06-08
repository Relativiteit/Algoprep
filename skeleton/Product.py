# For the product just multiply up to n-times, but start with n=6, so 2(*2*2*2*2*2*2) = 256 up to n-times
# In other words, how many times do I have to multiply 2 by 2 with when n=6? well 6
class Product:
    @staticmethod
    def iterative(n: int) -> int:
        raise NotImplementedError("Please implement me!")

    @staticmethod
    def recursive(n: int) -> int:
        raise NotImplementedError("Please implement me!")

# Test case(s):
n: int = 6
result: int = Product.iterative(n)
assert result == 128, f"got {result}, expected 128"

result = Product.recursive(n)
assert result == 128, f"got {result}, expected 128"