'''读写Json文件'''
import json
import random 
import function_readfile
import function_writefile
d={"a":'a',"b":2,'c':0.5,'d':[1,2,'y']}

def dump_():
    file_w=open('f.json','w+',encoding='utf-8')
    obj={"a":'a',"b":2}
    json.dump(d,file_w,indent=5)
    file_w.close()




def load():
    file_r=open('f.json')
    input('input... 1')
    json_str=json.load(file_r)
    input('input... 2')
    print(json_str)
    file_r.close()

print('b',9)
dump_()
for i in d:
    print(i)
print('b',99999)
load()
print('c',9)




