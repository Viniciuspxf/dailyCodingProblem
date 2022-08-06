def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
  return pair(lambda a, b : a)

def cdr(pair):
  return pair(lambda a, b : b)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))