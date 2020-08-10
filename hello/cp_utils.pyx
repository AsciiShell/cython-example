# distutils: language = c++

cdef extern from "hello_lib/library.cpp" namespace "hello":
    pass

cdef extern from "hello_lib/library.h" namespace "hello":
    cdef int hello(int, int)

def hello_cpfunc(int a, int b):
    return hello(a, b)
