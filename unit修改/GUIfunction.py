'''配合GUI.PY使用,用于读取\重置\保存数据,包括读取\重置\保存数据3个函数'''
import json
import define
txtfile=define.txtfile

def saveData(unitdict):
    ''' 将unitdict 写为txt文件'''
    gettabs= lambda n :'	' * n
    cs='		' #键和值之间的连接符号
    s=lambda string:'"'+str(string)+'"'
    def dicttostr(d:dict ,tab_n =0):
        '''将1个字典转换为可直接写入文件的字符串.\n
        d:输入的字典 ,
        tab_n:前面的缩进数'''
        rv =gettabs(tab_n) + '{'+'\n'
        for i in d:
            if type(d[i])==dict:
                rv=rv+ gettabs(tab_n+1) + s(i)+ '\n'+dicttostr(d[i],tab_n+1)
            else:
                rv=rv+ gettabs(tab_n+1) + s(i) + cs+ s(d[i])+'\n'
        rv=rv+gettabs(tab_n) + '}'+'\n'
        return rv 
    ##########################################
    f = open(txtfile, 'w')
    f.write('"DOTAUnits" \n')
    f.write(dicttostr(unitdict))
    f.close()
    print('保存数据完成')


