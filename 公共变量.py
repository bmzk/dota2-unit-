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
    '攻击类型  ': 'AttackDamageType',
    '英雄主属性  ': "AttributePrimary",
    '技能1  ': 'Ability1',
    '技能2  ': 'Ability2',
    '技能3  ': 'Ability3',
    '技能4  ': 'Ability4',
    '技能5  ': 'Ability5',
    '技能6  ': 'Ability6',
    '技能7  ': 'Ability7',
    # '技能8  ': 'Ability8',
    # '技能9  ': 'Ability9',
    '技能10  ': 'Ability10',
    '技能11  ': 'Ability11',
    '技能12  ': 'Ability12',
    '技能13  ': 'Ability13',
    '技能14  ': 'Ability14',
    '技能15  ': 'Ability15',
    '技能16  ': 'Ability16',
    '技能17  ': 'Ability17'
}

ChoiceItems_list_heroskill=[
'skill-1',
'skill-2'
]
ChoiceItems_list_spacialskill=[
'skill-11',
'skill-22'
]
import wx
wx.Choice
