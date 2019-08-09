
import define
import GUIfunction
import json
import wx
import function
import os

jsonfile = define.jsonfile
items = define.items
'''主程序，用于创建一个窗口界面'''


width = [150, 10, 100, 50, 50, 50, 50, 20,
         20, 20, 100, 100, 100, 100, 100, 100, 100]
head = ['', '基础值', '每级增加值', '遗迹', '圣坛']


class modify_zone(object):
    '''tower修改区域'''

    def __init__(self, panel, grid):
        # 表头

        for i in head:
            grid.Add(wx.TextCtrl(panel, value=i, style=wx.TE_READONLY | wx.TE_CENTER), pos=(
                0, head.index(i)), flag=wx.ALIGN_CENTER | wx.EXPAND)
        for i in items:
            grid.Add(wx.TextCtrl(panel, value=i, size=(150, -1), style=wx.TE_READONLY |
                                 wx.TE_CENTER), pos=(items.index(i)+1, 0), flag=wx.ALIGN_CENTER | wx.EXPAND)
        # 修改区域
        self.tc = []
        for i in range(len(items)):
            self.tc.append([])
            for j in range(len(head)-1):
                self.tc[i].append(wx.TextCtrl(panel, style=wx.TE_CENTER))
                grid.Add(self.tc[i][j], pos=(i+1, j+1), flag=wx.EXPAND)
        print('tower修改区域控件创建完毕')


class Mywin(wx.Frame):
    '''创建一个窗口类.\n'''

    def __init__(self):
        ''' 构造函数\n'''
        super(Mywin, self).__init__(
            None, title='Dota2 游戏数据修改', size=(800, 700))
        ################################################################
        #对象的属性#
        self.unit_dict = {}
        ###########################################################

        self.grid = wx.GridBagSizer(0, 0)  # 布局控件,其它控件将放在其内,用于单位显示属性
        self.panel = wx.Panel(self, -1)
        # add_modify_zone ##########################################################
        self.add_modify_zone(self.panel, self.grid)
        self.displaydata()
        #右侧窗口###################################################
        self.panel.SetSizerAndFit(self.grid)
        self.Center()
        self.Show()

    def add_modify_zone(self, panel, grid):
        # tower修改区域添加内容
        # 添加按钮 读取数据
        #self.读取数据 = wx.Button(panel, label="读取数据", style=wx.EXPAND)
        #self.grid.Add(self.读取数据, pos=(len(items)+2, 0))
        #self.读取数据.Bind(wx.EVT_BUTTON, self.check_readdata)
        # 添加按钮 保存数据
        self.保存数据 = wx.Button(panel, label="保存数据", style=wx.EXPAND)
        self.grid.Add(self.保存数据, pos=(len(items)+2, 2))
        self.保存数据.Bind(wx.EVT_BUTTON, self.check_savedata)
        # 添加数据区域
        self.zone = modify_zone(self.panel, self.grid)

    def displaydata(self):
        '''设置表格初始值\n'''
        # 设置表格初始值
        n = len(items)
        # 第1列
        # '护甲,DamageMin,DamageMax,攻速", "警戒距离","攻击距离", "hp", "生命恢复", "白天视野", "晚上视野"]
        ct1 = [15, 100, 150, 0.9, 700, 700, 5000, 10, 2000, 2000]
        for i in range(n):
            self.zone.tc[i][0].Value = str(ct1[i])
            # self.unit_dict['npc_dota_goodguys_tower1_top'][items[i]]

        # 第二列
        ct2 = [5, 50, 100, -0.1, 100, 100, 2500, 10, 500, 500]
        for i in range(n):
            self.zone.tc[i][1].Value = str(ct2[i])

        # 第3列
        ct3 = [40, 0, 0, 0, 0, 0, 12500, 100, 2500, 2500]
        for i in range(n):
            self.zone.tc[i][2].Value = str(ct3[i])
        # 第4列
        ct4 = [35, 0, 0, 0, 0, 0, 7500, 50, 0, 0]
        for i in range(n):
            self.zone.tc[i][3].Value = str(ct4[i])

    def check_savedata(self, Event):
        '''点击 保存数据按钮 时发生的事件'''
        # 读取json
        self.unit_dict = function.readjsonfile()
        #tower
        self.tower = []
        for i in ['1', '2', '3']:
            for j in ['top', 'mid', 'bot']:
                for k in ['good', 'bad']:
                    self.tower.append('npc_dota_'+k+'guys_tower'+i+'_'+j)
        self.tower.append("npc_dota_goodguys_tower4")
        self.tower.append("npc_dota_badguys_tower4")
        for i in self.tower:
            print(i)
        index=0
        vstr=[0,0,0]
        for i in self.tower:
            for j in items:
                index=items.index(j)
                try:
                     vstr[0]=int(self.zone.tc[index][0].Value)
                except :
                     vstr[0]=float(self.zone.tc[index][0].Value)
                try:
                   vstr[1]=int(self.zone.tc[index][1].Value)
                except :
                   vstr[1]=float(self.zone.tc[index][1].Value)
                vstr[2]=int(i[i.find('tower')+5])-1
                self.unit_dict[i][j] = vstr[0]+vstr[1]*vstr[2]
        #fort
        self.fort = ["npc_dota_goodguys_fort", "npc_dota_badguys_fort"]
        for i in self.fort:
            self.unit_dict[i]['ArmorPhysical'] = self.zone.tc[0][2].Value
            self.unit_dict[i]['StatusHealth'] = self.zone.tc[6][2].Value
            self.unit_dict[i]['StatusHealthRegen'] = self.zone.tc[7][2].Value
            self.unit_dict[i]['VisionDaytimeRange'] = self.zone.tc[8][2].Value
            self.unit_dict[i]['VisionNighttimeRange'] = self.zone.tc[9][2].Value
        # healer
        self.healer = ["npc_dota_goodguys_healers", "npc_dota_badguys_healers"]
        for i in self.healer:
            self.unit_dict[i]['ArmorPhysical'] = self.zone.tc[0][3].Value
            self.unit_dict[i]['StatusHealth'] = self.zone.tc[6][3].Value
            self.unit_dict[i]['StatusHealthRegen'] = self.zone.tc[7][3].Value

        #'''写入txt文件'''
        #print(self.unit_dict)
        GUIfunction.saveData(self.unit_dict)
        

def 启动窗口():
    app = wx.App()
    win = Mywin()
    app.MainLoop()


启动窗口()
