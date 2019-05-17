'''配合GUI.PY使用,用于读取\重置\保存数据,包括读取\重置\保存数据3个函数'''
import json
import 公共变量


def readData():
    '''从json文件中读取数据,返回值为字典,键值为 单位名,值为 属性组成的字典'''
    print('readData start')
    f = open(公共变量.jsonfile)
    unit_dict = json.load(f)['DOTAHeroes']
    unit_dict.pop('Version')
    # unitlist=list(unit_dict.keys())
    f.close()
    print('readData end')
    return unit_dict


def saveData(unitdict):
    ''' '''
    def dicttostr(d:dict ,tab_n =1):
        '''将1个字典转换为可直接写入文件的字符串.\n
        d:输入的字典 ,
        tab_n:前面的缩进数'''
        s=lambda string:'"'+string+'"'
        rv = '{'+'\n'
        for i in d:
            rv=rv+s(i)
            if type(d[i])==dict:
                rv=rv + '\n' + dicttostr(d[i])
            else :
                rv=rv+'		'+s(d[i])
                
        return rv 
    f = open('20190517.txt', 'w')
    f.write('"DOTAHeroes" \n')
    f.write('{\n')
    f.write('	"Version"		"1"\n')
    for i in unitdict:
        f.write('	"'+i+'"\n')  # i 是英雄名
        f.write('	{\n')
        for j in unitdict[i]:  # j 是属性名
            if type(unitdict[i][j]) == dict:
                f.write('		"'+j+'"\n')
                f.write('		{\n')
                for k in unitdict[i][j]:  # k是属性的属性名
                    if type(unitdict[i][j][k]) == dict:
                        f.write('			"'+k+'"\n')
                        f.write('			{\n')
                        for g in unitdict[i][j][k]:  # k是属性的属性的属性名
                            if type(unitdict[i][j][k][g]) == dict:
                                f.write('				"'+g+'"\n')
                                f.write('				{\n')
                                for h in unitdict[i][j][k][g]:
                                    f.write('					"'+h+'"		"' +
                                            str(unitdict[i][j][k][g][h])+'"\n')
                                f.write('					{\n')
                            else:
                                f.write('				"'+h+'"		"' +
                                        str(unitdict[i][j][k][g])+'"\n')
                        f.write('			}\n')
                    else:
                        f.write('			"'+k+'"		"'+str(unitdict[i][j][k])+'"\n')
                f.write('		}\n')
            else:
                f.write('		"'+j+'"		"'+str(unitdict[i][j])+'"\n')
    f.write('	}\n')
    f.write('}\n')
    f.close()
    print('保存数据完成')

def resetData(object):
    print('resetData')
    pass


def readToDb(sourceFile):
    sourceFile = myFile[:-4]+'备份'+thistime()+'.txt'
    # 数据库
    import pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["dota2"]  # 数据库数据库名称
    mycol = mydb["unit"]  # 数据库表名称
    # 插入一个文档（一行数据）
    mydict = {"name": "RUNOOB", "alexa": "10000",
              "url": "https://www.runoob.com"}

    for i in range(1, 10):
        mydict = {"name": str(i), "alexa": chr(
            x*x), "url": "https://www.runoob.com"}
        asd = mycol.insert_one(mydict)
        print(i, "", asd)
    pass

def cn_to_eng(cn: str):
    '''根据中文获取英文.\n'''
    rv = cn
    if cn.startswith('天赋'):
        rv = cn.replace('天赋','special_bonus')
    else:
        try:
            rv = 公共变量.translation[cn]
        except KeyError:
            print('错误,根据中文)获取英文,在翻译字典中未找到键值  cn =', cn)
            rv = 公共变量.str_null
        except:
            print('cn_to_eng  其他错误')
    return rv

def eng_to_cn(eng: str):
    '''根据英文获取中文.\n'''
    rv = eng
    if eng.startswith('special_bonus'):
        rv = eng.replace('special_bonus','天赋')
    else:
        for i in 公共变量.translation:
            if 公共变量.translation[i]==eng:
                rv = i
    return rv


'5.3'.isnumeric()
'3'.isnumeric()
'5.3'.isdigit()
'3'.isdigit()
