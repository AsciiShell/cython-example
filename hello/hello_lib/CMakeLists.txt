cmake_minimum_required(VERSION 3.17)
project(hello_lib)

set(CMAKE_CXX_STANDARD 14)

add_library(hello_lib library.cpp library.h)
add_executable(hello_lib_run library.cpp library.h)