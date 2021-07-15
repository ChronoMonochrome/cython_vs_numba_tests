import os
from time import time

os.chdir(r"F:\dev\python\numba")
from monte_carlo_numba import monte_carlo_pi as test_numba_pi
from monte_carlo_cy import monte_carlo_pi as test_cy_pi
from monte_carlo_py import monte_carlo_pi as test_py_pi

def time_monte_numba():
	t0 = time()
	test_numba_pi(100000)
	dt = time() - t0
	return dt

def time_monte_py():
	t0 = time()
	test_py_pi(100000)
	dt = time() - t0
	return dt

def time_monte_cy():
	t0 = time()
	test_cy_pi(100000)
	dt = time() - t0
	return dt

time_monte_numba()
nu = time_monte_numba()
py = time_monte_py()
cy = time_monte_cy()

print("pure: %f, numba: %f, cython: %f" %(py, nu, cy))