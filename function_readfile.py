'''读取文件,产生一个复制备份和一个json格式文件'''
def rf(r_file):
    '''读取文件,产生一个复制备份和一个json格式文件'''
    #产生复制文件
    import os
    import time
    t=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    newfile=r_file[:-4]+t+'备份.txt'
    os.system('copy '+r_file+' ' + newfile)
    #产生json文件
    f=open(r_file,'r',encoding='utf-8')
    print('正在读取源文件',r_file)
    lines = f.readlines()
    file_w=open('npc_heroes.json','w+',encoding='utf-8')
    print('正在读取json文件,文件为','npc_heroes.json')
    linelist=[]
    returnstring='{'
    for i in lines:
        linelist=i.split('"')
        #英雄和大类名字
        if len(linelist)== 3:
            returnstring = returnstring + '"'+ linelist[1] + '":'
        if len(linelist)== 5:
            returnstring = returnstring + '"'+ linelist[1] + '":"' + linelist[3]+'",'#+'\n'
        if i.find('{') != -1:
            returnstring = returnstring + '{'
        if i.find('}') != -1:
            returnstring = returnstring + '},'
    print('读取文件结束')
    returnstring = returnstring + '}'
    f.close()
    
    #去除错误
    returnstring = returnstring.replace(',\n}','\n}')
    returnstring = returnstring.replace(',}','}')
    returnstring = returnstring.replace('}','} \n')

    file_w.write(returnstring)
    file_w.close()
    print('生成json文件成功')
    return returnstring
