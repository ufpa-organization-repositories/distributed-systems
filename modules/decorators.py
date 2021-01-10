from typing import Callable, Any
from time import time, sleep
import PyQt5
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

import numpy as np
import scipy.stats

CONFIDENCE = 0.95

def mean_confidence_interval(data, confidence: float = 0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, h, m-h, m+h

DEBUG: bool = False # DEBUGs don't work at client side. ValueError: signal only works in main thread
N_PLOTS: int = 20

# img_count: int = None
img_count = 0 # Only use this line to storage all plots at once

def calc_time(function: Callable):
	"""
	# Decoration function: calculates the tima a function
	# takes to execute

	# Will be used to check the time took from each operation,
	# from 01 to 06 ones
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
		# result = function(*args, **kwargs) # the operation itself
		result = function(*args, **kwargs) # the operation itself
		end_time = time()

		exec_time = end_time - start_time		
		if DEBUG == True:
			print(f'time that the operation takes to execute: \n \
				>>>{exec_time}')

		# return result # the original return in function/operation
		return [result, exec_time] # to use without @calc_plot
		# return function()


	return wrapper

def calc_plot(function: Callable):	
	"""
	Decoration function: plots the graph of a time
	that a function takes to execute

	Will be used to plot the time took from each operation,
	from 01 to 06 ones
	"""

	def wrapper(*args, **kwargs) -> Any:		
		"""
		wraps/envolves the ...

		@calc_time
		operation function

		... retrieving the time it takes to execute
		of the @calc_time decorator

		return: Any -> Because can return both the result of the initial
		function, the result of the @calc_time decorator,
		or other anything return type defined in this wrapper
		(in this case, None, beacuse only displays the graph) 
		"""		
		li_exec_time: list = []		
		for i in range(N_PLOTS):
			results: List = function(*args, **kwargs) # returns the execution time
			result: Any = results[0]
			exec_time: float = results[1]
			li_exec_time.append(exec_time)

		m, h, m_less_h, m_pluss_h = mean_confidence_interval(data=li_exec_time,\
		 confidence=CONFIDENCE)		

		plt.figure(figsize=(12, 6))
		plt.plot(range(1, N_PLOTS + 1), li_exec_time)
		plt.axis(xmin=0, xmax=N_PLOTS + 1)
		plt.title(f'time per execution\nmean: {m}, delta: {h}\nP(m - delta:{m_less_h:.10f} < mean:{m:.10f} < m + delta:{m_pluss_h:.10f}) = {CONFIDENCE}')
		plt.ylabel('time (s)')
		plt.xlabel('executions')

		plt.scatter(range(1, N_PLOTS + 1), li_exec_time, marker='.',\
		 label="Execution", color="black")

		plt.scatter(1 + li_exec_time.index(min(li_exec_time)),\
		 min(li_exec_time), marker='s', label=f"Best time = {min(li_exec_time)} s",\
		  color="green")

		plt.scatter(1 + li_exec_time.index(max(li_exec_time)),\
		 max(li_exec_time), marker='*', label=f"Worst time = {max(li_exec_time)} s",\
		  color="red")

		plt.legend(bbox_to_anchor=(1, 1), loc='best', fancybox=True, framealpha=1)

		if DEBUG == True:
			print('ploting')
			plt.show()
			plt.close()
		else:
			print('saving')
			plt.savefig('time_operation.png')
			plt.close()
				
		return result

	return wrapper


# -------------------------------------
# testing

# """
# @calc_plot(debug=True) # TypeError: calc_plot() missing 1 required positional argument: 'function'
# @calc_plot # test with and without this
# @calc_time(debug=True) # test with and without this
# def operation(sleep_time: int = 1) -> str:	
# 	sleep(sleep_time)
# 	return f'sleep for {sleep_time} seconds'

# if __name__ == '__main__':
# 	result = operation(sleep_time=0.05)
	# print(result)
	# result.show()
# """