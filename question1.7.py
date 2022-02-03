import json
file="gudia.txt"
dic={}
with open(file) as f:
    for i in f:
        key,value=i.strip().split(None,1)
        dic[key]=value
b=open("meraki7.json","w")
json.dump(dic,b,indent=4)
b.close()