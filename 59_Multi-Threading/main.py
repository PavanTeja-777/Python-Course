import threading

def increment(counter, lock):
	for i in range(10000):
		with lock:
			counter[0] += 1

if __name__ == '__main__':
	counter = [0]  # Use a list to make counter mutable
	lock = threading.Lock()

	threads = []
	for i in range(3):
		thread = threading.Thread(target=increment, args=(counter, lock))
		threads.append(thread)
		thread.start()

	for thread in threads:
		thread.join()

	print('Counter value:', counter[0])

import threading

def thread_task(task):
    # Do some work here
    print(f'Task processed: {task}')

if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    threads = []
    for task in tasks:
        thread = threading.Thread(target=thread_task, args=(task,))
        threads.append(thread)

    for thread in threads:
        thread.start()
        thread.join()