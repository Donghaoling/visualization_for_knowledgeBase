f = open('E:\\knowledge_Base\\echarts\\topicwords\\topics_.json')
c = f.read()
lines = c.split('\n')
a = [2,4,9,10,14,15,20,25,31,38]
outwrite = []
print len(lines)
for i in range(0,len(a),1):
    outwrite.append(lines[a[i]-1])
with open('topics.txt','w') as f:
    f.write('\n'.join(outwrite))
    
