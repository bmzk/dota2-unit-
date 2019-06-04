def dicttostr(d:dict ,tab_n =0):
        '''将1个字典转换为可直接写入文件的字符串.\n
        d:输入的字典 ,
        tab_n:前面的缩进数'''
        cs=':' #键和值之间的连接符号
        s=lambda string:'"'+string+'"'
        gettabs= lambda n :'	' * n
        rv =gettabs(tab_n) + '{'+'\n'
        print(rv)
        for i in d:
            rv=rv + gettabs(tab_n+1) + s(i)
            if type(d[i])==dict:
                rv=rv + cs+ '\n' + dicttostr(d[i],tab_n+1)
            else :
                rv=rv+cs+s(d[i])
            rv=rv+',\n'
        # 最后一个元素没有','
        
        rv=rv[:len(rv)-2]
        rv=rv+'\n'+gettabs(tab_n)+'}\n'
        return rv 

d={
    "Version": "1",
    "BaseClass": "npc_dota_hero",
    "npc_dota_hero_axe": 
    {
        "AttackRange": "150",
        "AttributePrimary": "DOTA_ATTRIBUTE_STRENGTH",
        "BoundsHullName": "DOTA_HULL_SIZE_HERO",
        "ItemSlots": 
        {
            "DOTA": 
            {
                "SlotName": "head",
                "MaxPolygonsLOD1": "500"
            }
        }
    }
}
ss=dicttostr(d)
f=open('test.txt','w')
f.write(ss)
f.close()
print('end')