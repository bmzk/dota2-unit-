'''可视化界面'''


'''用于创建一个窗口界面,必须使用 GUI函数.py'''
'''设计思路:
1.整个窗口是1个对象,分为左侧窗口和右侧窗口
2.左侧窗口
3.右侧窗口所有控件作为1个对象
4.控件分为2个对象,一类是label+text,另一类是label+choice
'''
import wx

import function_readfile

items=['ArmorPhysical','AttackDamageMin',"AttackDamageMax","AttackRate","AttackAcquisitionRange","AttackRange","StatusHealth","StatusHealthRegen","VisionDaytimeRange","VisionNighttimeRange"]
width=[150,10,100,50,50,50,50,20,20,20,100,100,100,100,100,100,100]
head=['','基础值','每级增加值','遗迹','圣坛']

class Line(object):
    '''tower部分的一行'''
    def __init__(self, panel, mylabel=''):
        '''构造函数,创造一组控件,包括2个标签和2个文本框 \n'''
        self.linectrl_list=[]
        for i in head:
            self.linectrl_list.append(wx.TextCtrl(panel,style=wx.TE_CENTER|wx.EXPAND))
        self.linectrl_list[0]=wx.TextCtrl(panel,size=(150,-1),style=wx.TE_READONLY|wx.TE_CENTER)
        # self.linectrl_list[2]=wx.TextCtrl(panel,size=(60,-1),style=wx.TE_CENTER)
        # self.linectrl_list[3]=wx.TextCtrl(panel,size=(60,-1),style=wx.TE_CENTER)
        # self.linectrl_list[9]=wx.TextCtrl(panel,size=(60,-1),style=wx.TE_CENTER)
        # self.linectrl_list[10]=wx.TextCtrl(panel,size=(60,-1),style=wx.TE_CENTER)
class modify_zone(object):
    '''tower修改区域'''
    def __init__(self, panel, grid):
        #表头
        
        for i in head:
            grid.Add( wx.TextCtrl(panel, value=i,style=wx.TE_READONLY|wx.TE_CENTER), pos=(0,head.index(i)),flag=wx.ALIGN_CENTER|wx.EXPAND)
        for i in items[1:]:
            grid.Add( wx.TextCtrl(panel, value=i,size=(150,-1),style=wx.TE_READONLY|wx.TE_CENTER), pos=(items.index(i),0),flag=wx.ALIGN_CENTER|wx.EXPAND)    
        #修改区域
        for i in range(len(head)-1):
            for j in range(len(items)-1):
                grid.Add(wx.TextCtrl(panel,style=wx.TE_CENTER),pos=(j+1,i+1),flag=wx.EXPAND)
        print('tower修改区域控件创建完毕')

class Mywin(wx.Frame):
    '''创建一个窗口类.\n'''
    def __init__(self):
        ''' 构造函数\n'''
        super(Mywin, self).__init__(None, title='Dota2 游戏数据修改', size=(800, 700))
        ################################################################
        #对象的属性#
        self.unit_dict = {}
        self.unit_name_list = []
        self.SelectUnit = ''
        ###########################################################

        self.grid = wx.GridBagSizer(0, 0)  # 布局控件,其它控件将放在其内,用于单位显示属性
        self.panel = wx.Panel(self, -1)
        # add_modify_zone ##########################################################
        self.add_modify_zone(self.panel,self.grid)
        #右侧窗口###################################################
        self.panel.SetSizerAndFit(self.grid)
        self.Center()
        self.Show()

    def add_modify_zone(self,panel,grid):
        # tower修改区域添加内容
        #添加按钮 读取数据
        self.读取数据 = wx.Button(panel, label="读取数据",style=wx.EXPAND)
        self.grid.Add(self.读取数据,pos=(12,0))
        self.读取数据.Bind(wx.EVT_BUTTON, self.check_readdata)
        #空白
        self.zone=modify_zone(self.panel,self.grid)

        #单位列表



    def onRadioBox(self,event):
        rb = event.GetEventObject() 
        print (rb.GetLabel(),' is clicked from Radio Group' )
    def onChecked(self, event): 
            cb = event.GetEventObject() 
            print (cb.GetLabel(),' is clicked',cb.GetValue())
    def creat_json(self, event):
        function_readfile.rf(公共变量.file)

    def select_unit(self, event):
        self.SelectUnit = event.GetEventObject().GetStringSelection()
        self.Title = self.SelectUnit

        def refresh_att(linectrlslist):
            #i = linectrlslist[0]
            for i in linectrlslist:  # type(i) = linectrls
                i.selete_unit = self.unit_dict[self.SelectUnit]  # 选择的英雄的属性字典
                linectrlslist[linectrlslist.index(
                    i)].TextCtrl.SetLabel(i.value_cn())
        ##############################################
        for i in self.leftctrls:
            refresh_att(i.linectrlslist)
        for i in self.midctrls:
            refresh_att(i.linectrlslist)
        for i in self.rightctrls:
            refresh_att(i.linectrlslist)

    def check_readdata(self, Event):
        '''点击 读取数据按钮 时发生的事件'''
        self.unit_dict = GUI函数.readData()
        self.unit_name_list = list(self.unit_dict.keys())
        # print(self.unit_name_list)
        self.unit_name_list_box.Items = self.unit_name_list

    def check_savedata(self, Event):
        '''点击 保存数据按钮 时发生的事件'''

        for i in self.leftctrls:
            for j in i.linectrlslist:
                self.unit_dict[self.SelectUnit][j.key_eng()] = j.TextCtrl.GetLabelText()
        for i in self.midctrls:
            for j in i.linectrlslist:
                self.unit_dict[self.SelectUnit][j.key_eng()
                                                ] = j.TextCtrl.GetLabelText()
        for i in self.rightctrls:
            for j in i.linectrlslist:
                temp = j.Choice.GetStringSelection()
                if temp != '':
                    try:
                        temp = 公共变量.translation[temp]
                        self.unit_dict[self.SelectUnit][j.key_eng()] = temp
                    except:
                        print('check_savedata 错误, 公共变量.translation 无', temp)
        GUI函数.saveData(self.unit_dict)

    def add_ctrl(self, grid, panel):
        '''在右侧窗口添加控件以显示属性'''
        n = 6  # 左侧属性类别数量
        ############################################################
        # self.leftctrls是一个列表,元素类型为:ctrls,
        公共变量.currentline = 0
        leftattribute = list(公共变量.attribute_dict.keys())[:3]  # ['护甲','攻击']
        self.leftctrls = []
        for i in leftattribute:
            self.leftctrls.append(ctrls(panel, grid, i, 0, False, width=75))
            pass
        #######################################################
        公共变量.currentline = 0
        midtattribute = list(公共变量.attribute_dict.keys())[3:6]  # ['技能']
        self.midctrls = []
        for i in midtattribute:
            self.midctrls.append(ctrls(panel, grid, i, 2, False, width=75))
        #######################################################
        公共变量.currentline = 0
        rightattribute = list(公共变量.attribute_dict.keys())[-3:]  # ['技能']
        self.rightctrls = []
        for i in rightattribute:
            self.rightctrls.append(ctrls(panel, grid, i, 4, width=120))
        ########################################################
        # 添加保存按钮
        self.保存数据 = wx.Button(panel, label="保存数据")
        grid.Add(self.保存数据, pos=(公共变量.currentline+2, 5), flag=wx.ALIGN_CENTER)
        self.保存数据.Bind(wx.EVT_BUTTON, self.check_savedata)
        #添加按钮 重生成json
        self.重生成json = wx.Button(panel, label="重生成json")
        grid.Add(self.重生成json,  pos=(公共变量.currentline+2, 1), flag=wx.ALIGN_CENTER)
        self.重生成json.Bind(wx.EVT_BUTTON, self.creat_json)

def 启动窗口():
    app = wx.App()
    win = Mywin()
    app.MainLoop()

启动窗口()
