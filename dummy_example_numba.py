from numba import njit

@njit
def sane_function(input_list):
    output_list = []
    for item in input_list:
        if item % 2 == 0:
            output_list.append(2)
        else:
            output_list.append(1)
    return output_list

@njit
def test():
	test_list = list(range(100000))
	sane_function(test_list)[:5]