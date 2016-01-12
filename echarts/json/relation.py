import json
f = open('E:\\knowledge_Base\\echarts\\json\\nih.topwords.csv','r');
c = f.read();
f.close()
print c
topics = c.split(',');
print topics
relation = {};
for i in range(2005,2015,2):
    f1 = open('E:\\knowledge_Base\\echarts\\json\\'+str(i)+'.txt','r');
    c1 = f1.read()
    print c1
    index = c1.split('\n');
    print index
    ill = [];
    for j in range(0,50,1):
        dic = {};
        lis = [];
        lis = index[j].split(',');
        lis.append(2);
        lis = map(lambda x : x if type(x) == int else float(x)+1,lis)
        dic["name"] = topics[j];
        dic["value"] = lis; 
        ill.append(dic);
        print dic
    print ill
    relation[i] = ill;
print relation
f = open("relations3.json","w")
f.write("relations = ")
f.write(json.dumps(relation,sort_keys=True,indent=4).encode("utf-8"))
f.close()
