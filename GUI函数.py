'''配合GUI.PY使用,用于读取\重置\保存数据,包括读取\重置\保存数据3个函数'''
import json
import 公共变量


def readData():
    '''从json文件中读取数据,返回值为字典,键值为 单位名,值为 属性组成的字典'''
    print('readData start')
    f=open(公共变量.jsonfile)
    unit_dict=json.load(f)['DOTAHeroes']
    unit_dict.pop('Version')
    #unitlist=list(unit_dict.keys())
    f.close()
    print('readData end')
    return unit_dict

def saveData(unitdict):
    ''''''
    f=open('20190429.txt','w')
    f.write('"DOTAHeroes" \n')
    f.write('{\n')
    f.write('	"Version"		"1"\n')
    for i in unitdict:
        f.write('	"'+i+'"\n')  #i 是英雄名
        f.write('	{\n')
        for j in unitdict[i]:   #j 是属性名
            if type(unitdict[i][j]) == dict:
                f.write('		"'+j+'"\n')
                f.write('		{\n')
                for k in unitdict[i][j]:    #k是属性的属性名
                    if type(unitdict[i][j][k]) == dict:
                        f.write('			"'+k+'"\n')
                        f.write('			{\n')
                        for g in unitdict[i][j][k]: #k是属性的属性的属性名
                            if type(unitdict[i][j][k][g]) == dict:
                                f.write('				"'+g+'"\n')
                                f.write('				{\n')
                                for h in unitdict[i][j][k][g]:
                                    f.write('					"'+h+'"		"'+str(unitdict[i][j][k][g][h])+'"\n')
                                f.write('					{\n')
                            else:
                                f.write('				"'+h+'"		"'+str(unitdict[i][j][k][g])+'"\n')
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
    sourceFile=myFile[:-4]+'备份'+thistime()+'.txt'
    #数据库
    import pymongo 
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["dota2"]#数据库数据库名称
    mycol = mydb["unit"] #数据库表名称
    #插入一个文档（一行数据）
    mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }

    for i in range (1,10):
        mydict = { "name": str(i), "alexa":chr(x*x), "url": "https://www.runoob.com" }
        asd = mycol.insert_one(mydict) 
        print(i,"",asd)
    pass


