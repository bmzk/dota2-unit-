import json
def dump_(str):
    '''写入json文件'''
    file_w=open('f.json','w+',encoding='utf-8')
    
    json.dump(str,file_w,indent=5)
    file_w.close()



