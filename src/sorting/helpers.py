from time import time

def calculate_execution_time(func, param):
  start_time = time()
  func(param)
  end_time = time()

  execution_time = end_time - start_time

  print(f"Execution time: {execution_time:.10f}: seconds")