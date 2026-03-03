#opreater
class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, A):
            return A(self.value + other.value)
        return NotImplemented

    def __str__(self):
        return f"A({self.value})"
a1 = A(10)
a2 = A(20)
result = a1 + a2
print(result)  # Output: A(30)