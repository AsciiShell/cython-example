# cython-example

Simple project with c++/cython usage in a python.

The main goal of this project - demonstrate how c++ code could be build and used with python together. 
 
# hello

Demo methods in c++/cython/python languages are used together.

# Build 

```shell script
pip install -U pip setuptools Cython wheel
python setup.py sdist bdist_wheel
```

Install distribution:
```shell script
pip install hello-0.0.1.zip
hello
```

# License

MIT License

Copyright (c) 2020 AsciiShell