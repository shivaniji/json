import json
a={"a":6,"b":9,"c":3,"d":2,"e":"3j"}
with open ("shivani.json","w") as f:
    json.dump(a,f,indent=4)
print(type(a))
# b=json.dump(a)
# print(b)
# f=open()