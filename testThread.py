import time
import threading
#version: Python 3.4.1
def func(n):
	global count
	time.sleep(0.1)
	for i in range(n):
		count += 1
		
def sayHi():
	print("Hi, threading.")
		
if __name__ == "__main__":
	# count = 0
	# threads = []
	# for i in range(5):
		# threads.append(threading.Thread(target=func, args=(1000,)))
	# for t in threads:
		# t.start()
	# time.sleep(5)
	# print("count:", count)
	count = 0
	myThread = threading.Thread(target=func, args=(1000,))
	myThread.start()
	time.sleep(5)
	print("count:", count)
	
	testThread = threading.Thread(target=sayHi)
	testThread.start()
	
	while True:
		pass