def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
print(next(gen)) # 4

gen = my_generator()
for i in gen:
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4