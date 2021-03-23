
registry = []


def register(func):
    print(f'running register for {func}')
    registry.append(func)
    return func


@register
def f_1():
    print('f1 start')


@register
def f_2():
    print('f2 start')


@register
def f_3():
    print('f3 start')


def main():
    print(registry)
    f_1()
    f_2()
    f_3()


if __name__ == '__main__':
    main()
