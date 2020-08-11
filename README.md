# cython-example

Simple project with c++/cython usage in a python.

The main goal of this project - demonstrate how c++ code could be build and used with python together. 
 
# hello

Demo methods in c++/cython/python languages are used together.

# Build 

Create source distribution:
```shell script
python3 setup.py sdtist --formats zip,gztar
```

Install distribution:
```shell script
pip install hello-0.0.1.zip
hello
```

Create binary distribution (os dependent):
```shell script
python3 setup.py bdist
```

# License

MIT License

Copyright (c) 2020 AsciiShell