import math
a = 450    # градусы из условия
b = -690    
c = 780    
d = math.radians(a)  # перевод градусов в радианы
e = math.radians(b)  
f = math.radians(c)  
y = math.sin(d)+math.cos(e)*math.sin(f) # получение ответа
print(y)
