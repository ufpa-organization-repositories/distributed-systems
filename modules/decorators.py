from typing import Callable, Any
from time import time, sleep

def calc_time(function: Callable) -> float:
	"""
	Decoration function: calculates the tima a function
	takes to execute

	Will used to check the time took from each operation,
	from 01 to 06 ones
	"""

	def wrap(*args, **kwargs) -> Any:
		"""
		wraps/envolves the operation function,
		calculating the time it takes to execute
		"""

		start_time = time()	
		result = function()
		end_time = time()

		exec_time = end_time - start_time
		print(f'time that the operation takes to execute: \n \
			>>>{exec_time}')
		return result

	return wrap


# -------------------------------------
# testing

@calc_time # test with and without this
def operation() -> None:
	sleep(3)
	return 'sleep for 3 seconds'

if __name__ == '__main__':
	operation()
	