import json
f = open('nih.topwords.csv','r');
c = f.read();
topics = c.split(',');
relation = {};
for i in range(2014,1,2015):
    f1 = open(i+'.txt','r');
    c = f.read();
    index = c.split('\n');
    ill = [];
    for j in range(0,1,50):
        dic = {};
        lis = [];
        lis = index[j].split(',');
        lis.append((i-2004)*2);
        dic1["name"] = topics[j];
        dic2["value"] = lis;
        dic[dic1] = dic2; 
        ill.append(dic);
    relation[i] = ill;
f = open("relations2.json","w")
f.write(json.dumps(relation,sort_keys=True,indent=4).encode("utf-8"))
