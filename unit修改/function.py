'''读取dota2的txt文件,产生一个复制备份和一个json格式文件。'''
import os
import define
import json
sourcefile = define.sourcefile
jsonfile = define.jsonfile


def rf(r_file=sourcefile):
    '''读取文件,产生一个复制备份和一个json格式文件'''
    # 产生复制文件
    #file_backup(r_file)
    print("当前工作目录 : %s" % os.getcwd())
    # 产生json文件
    f = open(r_file, 'r', encoding='utf-8')
    print('正在读取源文件', r_file)
    lines = f.readlines()
    file_w = open(jsonfile, 'w+', encoding='utf-8')
    print('正在读取json文件,文件为', jsonfile)
    linelist = []  # 读取一行，以"为分隔符变为列表，存储在次列表中
    returnstring = '{'
    for i in lines:
        linelist = i.split('"')
        # 英雄和大类名字
        if len(linelist) == 3:
            returnstring = returnstring + '"' + linelist[1] + '":'
        if len(linelist) == 5:
            returnstring = returnstring + '"' + \
                linelist[1] + '":"' + linelist[3]+'",'  # +'\n'
        if i.find('{') != -1:
            returnstring = returnstring + '{'
        if i.find('}') != -1:
            returnstring = returnstring + '},'
    print('读取文件结束')
    returnstring = returnstring + '}'
    f.close()

    # 去除错误
    returnstring = returnstring.replace(',\n}', '\n}')
    returnstring = returnstring.replace(',}', '}')
    returnstring = returnstring.replace('}', '} \n')

    file_w.write(returnstring)
    file_w.close()
    print('生成json文件成功')
    return returnstring


def file_backup(myfile):
    '''产生一个备份文件,返回备份文件的文件名'''
    import time
    t = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    newfile = myfile[:-4]+t+'备份.txt'
    os.system('copy '+myfile+' ' + newfile)  # 复制文件
    return newfile

def readjsonfile(jf=jsonfile):
    '''读取json'''
    rf()
    f = open(jf)
    unit_dict = json.load(f)['DOTAUnits']
    #unit_dict.pop('Version')
    f.close()
    os.remove(jf)
    return unit_dict
print('导入 function_readfile 模块 成功')
