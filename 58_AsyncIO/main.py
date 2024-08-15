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