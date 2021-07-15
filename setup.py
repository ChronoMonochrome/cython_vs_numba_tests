from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("monte_carlo_cy.pyx")
)