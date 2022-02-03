import json


a={'4': 5, '6': 7, '1': 3, '2': 4}
b=sorted(a.items())
print(b)
d={}
for i in d:
    print(type(d))
d.update(b)
print(type(d))
n=json.dumps(d)
print(n)
print(type(n))


