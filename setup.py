__author__ = 'asciishell (Aleksey Podchezertsev)'
__maintainer__ = __author__

__email__ = 'mlao@asciishell.ru'
__license__ = 'MIT'
__version__ = '0.0.1'

import os
from importlib.machinery import SourceFileLoader

from setuptools import Extension, find_packages, setup

module_name = 'hello'
module = SourceFileLoader(
    module_name, os.path.join(module_name, '__init__.py')
).load_module()

try:
    from Cython.Build import cythonize

    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

ext = '.pyx' if USE_CYTHON else '.c'

extensions = [Extension('hello.cp_utils', ['hello/cp_utils' + ('.pyx' if USE_CYTHON else '.cpp')],
                        include_dirs=["hello/hello_lib/"],
                        extra_compile_args=["-std=c++14", "-O3"], language="c++"),
              Extension('hello.cy_utils', ['hello/cy_utils' + ('.pyx' if USE_CYTHON else '.c')],
                        extra_compile_args=["-std=c11", "-O3"], language="c")]

if USE_CYTHON:
    from Cython.Build import cythonize

    extensions = cythonize(extensions)

setup(
    name=module_name,
    version=__version__,
    author=__author__,
    author_email=__email__,
    license=__license__,
    description=__doc__,
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            '{0} = {0}.__main__:main'.format(module_name),
        ]
    },
    ext_modules=extensions,
    include_package_data=True,
    zip_safe=False,
)
