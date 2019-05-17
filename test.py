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
                rv=rv+':		'+s(d[i])
            rv=rv+',\n'
        # 最后一个元素没有','
        print(rv)
        rv=rv[:len(rv)-2]

        rv=rv+'\n}\n'
        return rv 

d={
    "DOTAHeroes": {
        "Version": "1",
        "npc_dota_hero_base": {
            "BaseClass": "npc_dota_hero",
            "BountyGoldMax": "0"
        },
        "npc_dota_hero_axe": {
            "AttackRange": "150",
            "AttributePrimary": "DOTA_ATTRIBUTE_STRENGTH",
            "BoundsHullName": "DOTA_HULL_SIZE_HERO",
            "ItemSlots": {
                "1": {
                    "SlotIndex": "1",
                    "SlotName": "head",
                    "SlotText": "#LoadoutSlot_Head_Accessory",
                    "TextureWidth": "256",
                    "TextureHeight": "256",
                    "MaxPolygonsLOD0": "1000",
                    "MaxPolygonsLOD1": "500"
                },
                "6": {
                    "SlotIndex": "6",
                    "SlotName": "summon",
                    "SlotText": "#LoadoutSlot_Pet",
                    "ShowItemOnGeneratedUnits": "1",
                    "GeneratesUnits": {
                        "0": "npc_dota_companion"
                    }
                }
            },
            "RenderablePortrait": {
                "Particles": {
                    "particles/units/heroes/hero_axe/axe_loadout.vpcf": "loadout"
                }
            },
            "Bot": {
                "SupportsEasyMode": "1",
                "Loadout": {
                    "item_stout_shield": "ITEM_CORE",
                    "item_platemail": "ITEM_LUXURY",
                    "item_mystic_staff": "ITEM_LUXURY",
                    "item_recipe_shivas_guard": "ITEM_LUXURY",
                    "item_shivas_guard": "ITEM_LUXURY | ITEM_DERIVED"
                },
                "Build": {
                    "1": "axe_counter_helix",
                    "2": "axe_berserkers_call",
                    "3": "axe_counter_helix"
                },
                "HeroType": "DOTA_BOT_TANK | DOTA_BOT_STUN_SUPPORT"
            }
        }
}}
ss=dicttostr(d)
f=open('test.json','w')
f.write(ss)
f.close()
print('end')