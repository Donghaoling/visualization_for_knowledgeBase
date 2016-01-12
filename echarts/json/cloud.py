import json
f = open('cloud.json','r')
c = f.read()
f.close()
c = c[c.find('=')+1:]
print c
f.close()
d = json.loads(c)
out = []
for i in range(0,10,3): 
    out.append(d[i][:4])
f = open('cloud4.json','w')
f.write(json.dumps(out,sort_keys=True,indent=4).encode("utf-8"))
f.close()
