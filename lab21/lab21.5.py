import functools
numbers=[20,30,10,40]
results=functools.reduce(lambda x,y:x+y,numbers)
print(results)