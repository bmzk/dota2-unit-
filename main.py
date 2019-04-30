#
mydict = {
    '力量+': 'strength',
    '敏捷+': 'agility',
    '智力+': 'intelligence',
    '全属性+': 'all_stats',

    '生命+': 'hp',
    '生命恢复+': 'hp_regen',
    '魔法+': 'mp',
    '魔法恢复+': 'mp_regen',

    '攻击+':'attack',
    '攻击速度+':'attack_speed',
    '护甲+':'armor',
    '移速+':"movement_speed"
    }

f = open('temp.txt', 'w+', encoding='utf-8')
mystr = ''
n = 0
special_bonus_dict={}
for j in mydict:
    for i in range(100):
        if l2[j] == 'hp' or l2[j] == 'mp':
            n = i*10+10
        else:
            n = i+1
        mystr = '"'+l1[j]+str(n)+'" : "special_bonus_'+l2[j]+'_'+str(n)+'",\n'
        f.write(mystr)
        print(mystr)
f.close()
