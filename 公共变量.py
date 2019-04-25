import wx
'''定义公共变量'''
file = 'npc_heroes.txt'
file = 'npc.txt'
jsonfile = 'npc_heroes.json'

attribute_name_dict = {
    '物理护甲  ': 'ArmorPhysical',
    '魔法护甲  ': 'MagicalResistance',
    '最小攻击力  ': 'AttackDamageMin',
    '最大攻击力  ': 'AttackDamageMax',
    '攻击速度  ': 'AttackRate',
    '主动攻击距离  ': 'AttackAcquisitionRange',
    '攻击距离  ': 'AttackRange',
    '移动速度  ': 'MovementSpeed',
    '初始生命值  ': 'StatusHealth',
    '生命恢复速度  ': 'StatusHealthRegen',
    '初始魔法值  ': 'StatusMana',
    '魔法恢复速度  ': 'StatusManaRegen',
    '初始力量  ': "AttributeBaseStrength",
    '力量成长  ': "AttributeStrengthGain",
    '初始智力  ': "AttributeBaseIntelligence",
    '智力成长  ': "AttributeIntelligenceGain",
    '初始敏捷  ': "AttributeBaseAgility",
    '敏捷成长  ': "AttributeAgilityGain",
    '白天视野  ': 'VisionDaytimeRange',
    '夜间视野  ': 'VisionNighttimeRange'
}


skill_dict = {
    '技能1  ': 'Ability1',
    '技能2  ': 'Ability2',
    '技能3  ': 'Ability3',
    '技能4  ': 'Ability4',
    '技能5  ': 'Ability5',
    '技能6  ': 'Ability6',
}
special_bonus_dict = {
    '10级 右侧  ': 'Ability10',
    '10级 左侧  ': 'Ability11',
    '15级 右侧  ': 'Ability12',
    '15级 左侧  ': 'Ability13',
    '20级 右侧  ': 'Ability14',
    '20级 左侧  ': 'Ability15',
    '25级 右侧  ': 'Ability16',
    '25级 左侧  ': 'Ability17'
}

ChoiceItems_list_AttributePrimary = [
    'Null',
    'DOTA_ATTRIBUTE_STRENGTH',
    'DOTA_ATTRIBUTE_AGILITY',
    'DOTA_ATTRIBUTE_INTELLECT',
]

ChoiceItems_list_AttackCapabilities = [
    'Null',
    '近程\n DOTA_UNIT_CAP_MELEE_ATTACK',
    '远程\n DOTA_UNIT_CAP_RANGED_ATTACK'
]


ChoiceItems_list_skill = [
    'Null',
    'pudge',
    '决斗'
]

ChoiceItems_list_special_bonus = [
    'Null',
    'special_bonus_movement_speed_30',
    'special_bonus_movement_speed_50'

]