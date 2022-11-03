def n_fibonacci_recursive(n):
    if n < 0:
        raise ValueError("Number n must be a positive integer")
    elif n < 2:
        return n
    else:
        return n_fibonacci_recursive(n - 1) + n_fibonacci_recursive(n - 2)


def n_fibonacci_iterative(n):
    if n < 0:
        raise ValueError("Number n must be a positive integer")
    elif n == 0:
        return 0
    else:
        n1 = 0
        n2 = 1
        nth = n1 + n2
        for _ in range(n - 2):
            n1 = n2
            n2 = nth
            nth = n1 + n2
        return nth


cache = {}


def n_fibonacci_dict(n):
    if n < 0:
        raise ValueError("Number n must be a positive integer")
    elif n < 2:
        return n
    elif n in cache:
        return cache[n]
    else:
        resultado = n_fibonacci_dict(n - 1) + n_fibonacci_dict(n - 2)
        cache[n] = resultado
        return resultado


def s_fibonacci(n):
    for i in range(n + 1):
        print(n_fibonacci_iterative(i))


print(n_fibonacci_iterative(9))
print(n_fibonacci_recursive(9))
print(n_fibonacci_dict(9))


def test_fibonacci_of_9():
    expected = 34
    actual = n_fibonacci_iterative(9)
    if actual == expected:
        print("OK!")
    else:
        print("Fail")


def test_fibonacci_of_12():
    expected = 144
    actual = n_fibonacci_iterative(12)
    if actual == expected:
        print("OK!")
    else:
        print("Fail")
