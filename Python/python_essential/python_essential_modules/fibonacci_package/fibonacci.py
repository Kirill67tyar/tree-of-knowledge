__all__ = (
    'endless_fibonacci', 'fibonacci',
)


def endless_sequence():
    first, second = 0, 1
    while True:
        yield second
        first, second = second, first + second


def fibonacci(value):
    generator = endless_sequence()
    for i in range(value):
        yield next(generator)


def nth_fibonacci(value):
    result = None
    for current in fibonacci(value):
        result = current
    return result

pkg = __package__

if __name__ == '__main__':
    # for num in endless_sequence():
    #     print(num)
    #     if num > 10000:
    #         break
    # print('-' * 50)
    # fib10 = fibonacci(10)
    # print(fib10)
    # for num in fib10:
    #     print(num)
    # print('-' * 50)
    # print(nth_fibonacci(11))
    pass