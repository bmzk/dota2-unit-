import json
import random
import function_readfile
import function_writefile
import 公共变量
import GUI
import GUI函数
import wx
#读取txt文件生成json文件
str = function_readfile.rf(公共变量.file)
#启动窗口,显示单位及其属性
def test():
    app = wx.App()
    win = GUI.Mywin()
    '''点击 读取数据按钮 时发生的事件'''
    win.unit_dict = GUI函数.readData()
    win.unit_dict['npc_dota_hero_base']["ArmorPhysical"]='256789'
    GUI函数.saveData(win.unit_dict)

test()