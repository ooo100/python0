import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
x = datetime.datetime(2020, 9, 14)
print(x)
import datetime
x = datetime.datetime(2020, 9, 14)
print(x.strftime("%B"))
x = min(1,2,3)
y = max(1,2,3)
print(x)
print(y)
x = abs(-10)
print(x)
x = pow(2, 3)
print(x)
import math
x = math.sqrt(4)
print(x)
import json
x = '{"name" : "wow", "age" : 50}'
y = json.loads(x)
print(y["name"])
import camelcase
a = camelcase.Camelcase()
txt = "Oh wow"
print(a.hump(txt))
"""try:
  print(p)
except:
  print("An exception occurred)
name = input("name: ")
print("Your name: " + name)
age = 100
txt = "Your age is {} ."
print(txt.format(age))
a = 30
b = 40
c = 50
xxx = "like {}, and {}, also {}."
print(xxx.format(a, b, c))"""