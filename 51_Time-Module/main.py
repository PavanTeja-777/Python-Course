import time

print(time.time()) # Time elasped from where time module has been initliazed

print("Start:", time.time())
time.sleep(2) # Program halts for 2 seconds
print("End:", time.time())

# Prints local time
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)