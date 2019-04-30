#
l1=  [    '加力量',
    '加敏捷',
    '加智力',
    '加全属性',

    '加生命',
    '加生命恢复',
    '魔法',
    '魔法恢复',

    '加攻击',
    '加攻击速度',
    '加护甲',
    '加移速']

l2=['strength','agility','intelligence','all_stats',
'hp','hp_regen','mp','mp_regen',
'attack','attack_speed','armor',
'movement_speed']
for j in range(len(l1)):
    for i in range(100):
        print('"'+l1[j],str(i)+'" : "special_bonus_'+l2[j]+'_'+str(i)+
        '",')