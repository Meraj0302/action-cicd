# def sum(a,b):
#     print(a+b)

# def multi(x,y):
#     print(x*y)

# sum(10,20)

# multi(5,2)



def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def multiply(x: int, y: int) -> int:
    """Return the product of two numbers."""
    return x * y


if __name__ == "__main__":
    result_sum = add(10, 20)
    result_multi = multiply(5, 2)

    print("Sum:", result_sum)
    print("Multiplication:", result_multi)