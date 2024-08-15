# Async IO
- Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner.
- In Python, async programming is achieved through the use of the `asyncio` module and asynchronous functions.
- With the `asyncio` module and asynchronous functions, you can write efficient and scalable code that can handle large amounts of data and I/O operations without blocking the main thread.
- Whether you're working on web applications, network services, or data processing pipelines, async IO is an essential tool for any Python developer.
## Example
Suppose we want to make a download manager app using Python
- if we use traditional methods the files will download one after another
- if we use AsyncIO all files will download concurrently
```py
import asyncio

async def downloadFile(url):
	# Assume this contains code
	# to download a file from url
	await asyncio.sleep(10) 
	print('Done')

async def main():
	await asyncio.gather(
			downloadFile('url1'),
			downloadFile('url2'),
			downloadFile('url3'),
		)

asyncio.run(main())
```
