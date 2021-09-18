def number_generator():
    yield 0
    yield 1
    yield 2
    yield "string"
 
for i in number_generator():
    print(i)
    
g = number_generator()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

def foo(a, b = None):
    if b is None:
        b = [0]
    print(b)
    
foo(1,[2])
foo(1)

set = {2,4,1}
print(set)
set