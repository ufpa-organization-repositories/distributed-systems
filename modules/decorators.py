from typing import Callable, Any
from time import time, sleep
# from matplotlib import pyplot


def calc_time(debug: bool = True) -> float:
	"""
	Decorator Factory Design Pattern
	Used to receive the argument debug
	"""

	def decorator(function: Callable) -> Callable:
		"""
		Decoration function: calculates the tima a function
		takes to execute

		Will be used to check the time took from each operation,
		from 01 to 06 ones
		"""

		def wrapper(*args, **kwargs) -> Any:
			"""
			wraps/envolves the operation function,
			calculating the time it takes to execute
			return: Any -> Because can return both the result of the initial
			function or other anything return type defined in this wrapper
			(in this case, the time of execution of the function) 
			"""

			start_time = time()	
			result = function(*args, **kwargs) # the operation itself
			end_time = time()

			exec_time = end_time - start_time
			if debug == True:
				print(f'time that the operation takes to execute: \n \
					>>>{exec_time}')

			# return result # the original return in function/operation
			return exec_time # to use without @calc_plot
			# return function()


		return wrapper

	# return decorator(function)
	return decorator

def calc_plot(function: Callable, debug = 'debug printed'):	
	"""
	Decorator Factory Design Pattern to 
	plot a time an operation takes to
	execute
	"""

	# def decorator(function: Callable) -> Callable:		
	# 	"""
	# 	Decoration function: plots the graph of a time
	# 	that a function takes to execute

	# 	Will be used to plot the time took from each operation,
	# 	from 01 to 06 ones
	# 	"""
	def wrapper(*args, **kwargs):
		result: float = function(*args, **kwargs) # returns the execution time
		print(result)
		print(debug)
		return 'ploted'

	return wrapper
# -------------------------------------
# testing

@calc_plot # test with and without this
@calc_time(debug=True) # test with and without this
def operation(sleep_time: int = 1) -> str:	
	sleep(sleep_time)
	return f'sleep for {sleep_time} seconds'

if __name__ == '__main__':
	result = operation(sleep_time=2)
	print(result)
	