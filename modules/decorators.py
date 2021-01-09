from typing import Callable, Any
from time import time, sleep


def calc_time(debug: bool = True) -> float:
	"""
	Decorator Factory Design Pattern
	Used to receive the argument debug
	"""

	def decorator(function: Callable) -> Callable:
		"""
		Decoration function: calculates the tima a function
		takes to execute

		Will used to check the time took from each operation,
		from 01 to 06 ones
		"""

		def wrapper(*args, **kwargs) -> Any:
			"""
			wraps/envolves the operation function,
			calculating the time it takes to execute
			"""

			start_time = time()	
			result = function(*args, **kwargs)
			end_time = time()

			exec_time = end_time - start_time
			if debug == True:
				print(f'time that the operation takes to execute: \n \
					>>>{exec_time}')
			return result

		return wrapper

	return decorator


# -------------------------------------
# testing

@calc_time(debug=False) # test with and without this
def operation() -> None:
	sleep_time = 3
	sleep(sleep_time)
	return f'sleep for {sleep_time} seconds'

if __name__ == '__main__':
	result = operation()
	print(result)
	