from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='sieve', 
    ext_modules=cythonize('sieve_ct.pyx')
    )
