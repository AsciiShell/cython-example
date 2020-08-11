from setuptools import Extension, find_packages, setup

try:
    from Cython.Build import cythonize

    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

module_name = 'hello'

extensions = [Extension('hello.cp_utils', ['hello/cp_utils' + ('.pyx' if USE_CYTHON else '.cpp')],
                        include_dirs=['hello/hello_lib/'],
                        extra_compile_args=['-std=c++14', '-O3'], language='c++'),
              Extension('hello.cy_utils', ['hello/cy_utils' + ('.pyx' if USE_CYTHON else '.c')],
                        extra_compile_args=['-std=c11', '-O3'], language='c')]

if USE_CYTHON:
    extensions = cythonize(extensions)

with open('README.md', 'rt') as f:
    long_description = f.read()

setup(
    name=module_name,
    version='0.0.2',
    description='A sample Python project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AsciiShell/cython-example',
    author='asciishell (Aleksey Podchezertsev)',
    author_email='mlao@asciishell.ru',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: C++',
        'Programming Language :: Cython',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft',
    ],
    keywords=['python python3 cython cpp mit-license'],
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            '{0} = {0}.__main__:main'.format(module_name),
        ]
    },

    ext_modules=extensions,
    include_package_data=True,
    zip_safe=False,
)
