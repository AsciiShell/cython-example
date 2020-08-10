from hello.py_utils import hello_pyfunc
from hello.cy_utils import hello_cyfunc
from hello.cp_utils import hello_cpfunc


def main():
    print('Hello, world!')
    print(hello_cyfunc(10, 20))
    print(hello_cpfunc(10, 20))
    print(hello_pyfunc(10, 20))


if __name__ == '__main__':
    main()
