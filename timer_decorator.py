import time

def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		print(f'fun took {round(time.time() - start, 4)} seconds')
	return wrapper


@timer
def myprinter(textToPrint):
	print(textToPrint)


(myprinter("Kolbasz"))

