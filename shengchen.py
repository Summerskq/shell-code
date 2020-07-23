"""
result = []
for x in range(1,11):
   y = 2*x+8
   result.append(y)
print(result)
"""

"""
s = [2*x+8 for x in range(1,11)]
print(s)

"""
"""
s = [2*x+8 for x in range(1,11) if x%2 == 0]
print(s)
"""
"""
s = {x**2 for x in range(1,11)}
print(s)
print(type(s))
"""

s = {x:x**2 for x in range(1,11)}
print(s)
print(type(s))

