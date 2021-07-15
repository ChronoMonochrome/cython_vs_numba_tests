import timeit

numba_time = timeit.timeit("dummy_example_numba.test()", setup = "import dummy_example_numba", number = 1)
py_time = timeit.timeit("dummy_example_py.test()", setup = "import dummy_example_py", number = 1)

print(numba_time, py_time)