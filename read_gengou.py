import json
import codecs

a = codecs.open('gengou.json','r','utf-8')
b = json.load(a)
print(b)