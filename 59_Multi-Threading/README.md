# Multithreading

- Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process.
- In Python, we can use the threading module to implement multithreading. In this tutorial, we will take a closer look at the threading module and its various functions and how they can be used in Python.

## Importing Threading
We can use threading by importing the threading module.

```py
import threading
```

## Creating a Thread
- To create a thread, we need to create a Thread object and then call its `start()` method.
- The `start()` method runs the thread and then to stop the execution, we use the `join()` method. Here's how we can create a simple thread.

```py
import threading

def my_func():
	print('Hello from thread', threading.current_thread().name)
	thread = threading.Thread(target=my_func)
	thread.start()
	thread.join()
```

## Creating Multiple Threads
- Creating multiple threads is a common approach to using multithreading in Python. The idea is to create a pool of worker threads and then assign tasks to them as needed.
- This allows you to take advantage of multiple CPU cores and process tasks in parallel.

```py
import threading

def thread_task(task):
	# Do some work here
	print(f'Task processed: {task}')

tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

threads = []
for task in tasks:
	thread = threading.Thread(target=thread_task, args=(task,))
	threads.append(thread)

for thread in threads:
	thread.start()
	thread.join()
```

## Using a lock to synchronize access to shared resources
- When working with multithreading in python, locks can be used to synchronize access to shared resources among multiple threads.
- A lock is an object that acts as a semaphore, allowing only one thread at a time to execute a critical section of code. The lock is released when the thread finishes executing the critical section.

```py
import threading

def increment(counter, lock):
	for i in range(10000):
		with lock:
			counter[0] += 1

counter = [0]
lock = threading.Lock()

threads = []
for i in range(5):
	thread = threading.Thread(target=increment, args=(counter, lock))
	threads.append(thread)

for thread in threads:
	thread.start()
	thread.join()

print('Counter value:', counter[0])
```