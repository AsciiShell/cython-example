#include "library.h"

#include <iostream>

namespace hello {
    int hello(int a, int b) {
        return a + b;
    }
}

int main(int argc, char **argv) {
    std::cout << hello::hello(10, 20) << std::endl  ;
    return 0;
}