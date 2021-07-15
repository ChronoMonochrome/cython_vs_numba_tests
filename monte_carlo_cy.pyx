import random

cpdef float monte_carlo_pi(int nsamples):
	cdef float x, y
	cdef float acc = .0
	cdef int i

	for i in range(nsamples):
		x = random.random()
		y = random.random()
		if (x ** 2 + y ** 2) < 1.0:
			acc += 1.
	return 4.0 * acc / nsamples