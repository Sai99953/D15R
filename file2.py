def add(a,b):
  return a+b
print(add(10,35))

def mul(a,b):
  yield a*b
print(next(mul(25,6)))
  
