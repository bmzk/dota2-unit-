'''定义公共变量'''
file = 'npc_heroes.txt'
file = 'npc.txt'
jsonfile = 'npc_heroes.json'

#属性字典#
attribute_dict = {
    '护甲': ['物理护甲', '魔法抗性'],
    '攻击': ['最小攻击力', '最大攻击力', '攻击速度', '主动攻击范围', '攻击距离'],
    '属性': ['初始力量', '力量成长', '初始智力', '智力成长', '初始敏捷', '敏捷成长'],
    '移速': ['移动速度'],
    '状态': ['初始生命值', '生命恢复速度', '初始魔法值', '魔法恢复速度'],
    '视野': ['白天视野', '夜间视野'],

    #################################

    '技能': ['技能1', '技能2', '技能3', '技能4', '技能5', '技能6'],
    '天赋': ['10级右', '10级左', '15级右', '15级左', '20级右', '20级左', '25级右', '25级左'],
    '英雄主属性': ['英雄主属性'],
    ###############################
    'null': []
}

choiceitems_dict = {
    '技能': ['','pudge_flesh_heap','lion_finger_of_death', '技能3', '技能4', '技能5', '技能6'],
    '天赋': ['','10级右', '10级左', '15级右', '15级左', '20级右', '20级左', '25级右', '25级左'],
    '英雄主属性': ['','力量', '敏捷', '智力'],
    ###############################
    'null': []
}

translation = {
    ####左侧##########################################
    #护甲#
    '物理护甲': 'ArmorPhysical',
    '魔法抗性': 'MagicalResistance',
    #攻击#
    '最小攻击力': "AttackDamageMin",
    '最大攻击力': "AttackDamageMax",
    '攻击速度': "AttackRate",
    '主动攻击范围': "AttackAcquisitionRange",
    '攻击距离': "AttackRange",

    #属性###########################
    '力量成长': "AttributeStrengthGain",
    '初始智力': "AttributeBaseIntelligence",
    '智力成长': "AttributeIntelligenceGain",
    '初始敏捷': "AttributeBaseAgility",
    '敏捷成长': "AttributeAgilityGain",
    #'移动速度'#
    '移动速度': "MovementSpeed",
    #状态#
    '初始生命值': "StatusHealth",
    '生命恢复速度': "StatusHealthRegen",
    '初始魔法值': "StatusMana",
    '魔法恢复速度': "StatusManaRegen",
    #视野#
    '白天视野': 'VisionDaytimeRange',
    ####右侧##########################################
    #技能#
    '技能1': 'Ability1',
    '技能2': 'Ability2',
    '技能3': 'Ability3',
    '技能4': 'Ability4',
    '技能5': 'Ability5',
    '技能6': 'Ability6',
    # 天赋
    '10级右': 'Ability10',
    '10级左': 'Ability11',
    '15级右': 'Ability12',
    '15级左': 'Ability13',
    '20级右': 'Ability14',
    '20级左': 'Ability15',
    '25级右': 'Ability16',
    '25级左': 'Ability17',
    # 主属性
    '英雄主属性': "AttributePrimary",
    #### 其他 ##########################################
    '力量': "DOTA_ATTRIBUTE_STRENGTH",
    '敏捷': "DOTA_ATTRIBUTE_AGILITY",
    '智力': "DOTA_ATTRIBUTE_INTELLECT",
    #### 结尾 ##########################################
    'null': 'null'
}


def t():
    '''自动反转 translation的属性与值'''
    l1 = list(translation.keys())
    l2 = list(translation.values())
    for i in l1:
        print(i, l2[l1.index(i)])
