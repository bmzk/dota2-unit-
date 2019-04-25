'''用于创建一个窗口界面,必须使用 GUI函数.py'''
'''设计思路:
1.整个窗口是1个对象,分为左侧窗口和右侧窗口
2.左侧窗口
3.右侧窗口所有控件作为1个对象
4.控件分为2个对象,一类是label+text,另一类是label+choice
'''
import wx

import GUI函数
import 公共变量

class LineCtrls(object):
    '''创建创造一个控件对象,包括StaticText \TextCtrl \wx.Choice控件'''
    def __init__(self, panel,  width,ChoiceList=[]):
        '''构造函数,创造一组控件,包括2个标签和2个文本框 \n
        StaticText_str:标签中的文字列表
        panel=wx.Panel()'''
        # 创建一个标签,坐标(n,0)
        self.StaticText = wx.StaticText(panel,style=wx.ALIGN_RIGHT)
        self.StaticText.SetBackgroundColour('white') #背景色
        self.TextCtrl=wx.TextCtrl(panel, size=(width, -1),style=wx.TE_CENTER)
        self.Choice = wx.Choice(panel,choices=ChoiceList)
class CtrlList():
    '''创造一组包含n个LineCtrls对象的列表'''
    def __init__(self,panel,grid,StartPos=(0,0),n=5,IsHasChoice=False ,width=100,ChoiceList=[]):
        '''n: CtrlList包含的控件个数
        IsTextCtrl : 要TextCtrl还是Choic,默认TextCtrl'''
        self.clist=[]
        for i in range(n):
            self.clist.append(LineCtrls(panel,width,ChoiceList))
        for i in self.clist:
            x=StartPos[0]+self.clist.index(i)
            print(x,StartPos[1])
            grid.Add(i.StaticText ,pos=(x,StartPos[1]  ),flag= wx.ALIGN_CENTER | wx.ALL)
            grid.Add(i.TextCtrl   ,pos=(x,StartPos[1]+1),flag= wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)
            if IsHasChoice:
                grid.Add(i.Choice ,pos=(x,StartPos[1]+2),flag= wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)

class  Mywin(wx.Frame):
    '''创建一个窗口类.\n
    '''
    def __init__(self):
        '''构造函数\n
        GridBagSizer : 子构件可被添加到网格中的特定单元.
        一个子物件可以在水平和/或垂直地占据一个以上的单元.
        主要使用方法 : Wx.GridbagSizer().Add(control, pos, span, flags, border) \n
        control : 控件 \n
        pos : 控件位置,第几行第几列,从0开始\n
        span : 控件跨越的行数和列数\n
        '''
        super(Mywin, self).__init__(
            None, title='Dota2 游戏数据修改', size=(800, 650))
        ################################################################
        #对象的属性#
        self.error_str = ['无此键值','错误键值']  # 读取属性时出现不存在的属性显示键值
        self.unit_dict = {}
        self.unit_name_list = []
        self.SelectUnit=''
        ################################################################
        # 分离器对象添加到顶层帧。
        # 一个布局管理器，拥有两个子窗口,子窗口大小可以通过拖动它们之间的界限来动态变化。
        splitter = wx.SplitterWindow(self, -1)
        #左侧窗口###################################################
        self.panel_left = wx.Panel(splitter, -1)
        self.grid_left = wx.BoxSizer(wx.VERTICAL)  # 左侧的窗口,用于显示 单位名称
        '''hbox.Add(wx.Window window, integer proportion=0, integer flag = 0, integer border = 0)
        window：需要添加到wx.BoxSizer的控件；
        proportion：定义了控件在既定方向上相对于相对于其他组件所占空间的比例，
            比如：在水平sizer中有三个按钮，porportion=0，表示保持本身大小；
            porportion=1，表示在水平方向上占三分之一的空间；porportion=2，
            表示在水平方向上占三分之二的空间。
        flag：flag参数定义了两个主要的行为：第一个参数是窗口的边框：
            这个参数决定了边框的宽度，在此决定窗口某一侧添加边框的事件。
            另一个参数决定了sizer事件的行为，当sizer改变时，空间的分配。
            并且分配的多少依赖于特定种类的sizer被使用。
            flag参数可以使用 '|'来产生组合的多个flags。
            常用的flag参数：wx.TOPwx.BOTTOMwx.LEFTwx.RIGHTwx.ALLwx.EXPAND
        border：调整控件的边框的宽度，此参数一般和flag参数配合使用。'''
        # 左侧窗口添加内容
        self.读取数据 = wx.Button(self.panel_left, label="读取数据")
        self.grid_left.Add(self.读取数据, 0)
        self.label_ = wx.StaticText(
            self.panel_left, label='', style=wx.ALIGN_CENTER)
        self.grid_left.Add(self.label_, 0)
        self.unitlabel = wx.StaticText(self.panel_left, label='选择单位')
        self.grid_left.Add(self.unitlabel, 0)
        self.unit_name_list_box = wx.ListBox(
            self.panel_left, choices=self.unit_name_list, style=wx.LB_SINGLE)
        self.grid_left.Add(self.unit_name_list_box, 90)
        # 绑定数据
        self.读取数据.Bind(wx.EVT_BUTTON, self.check_readData)
        self.Bind(wx.EVT_LISTBOX, self.select_unit,
                  self.unit_name_list_box)  # 绑定,点击左侧选择项时发生事件
        ############################################################
        #右侧窗口###################################################
        self.grid_right = wx.GridBagSizer(0, 0)  # 右侧布局控件,其它控件将放在其内,用于单位显示属性
        self.panel_right = wx.Panel(splitter, -1)
        # 右侧窗口添加内容
        self.add_ctrl(self.grid_right, self.panel_right)
        ###########################################################
        # self.Show()
        splitter.SplitVertically(self.panel_left, self.panel_right)
        self.panel_left.SetSizerAndFit(self.grid_left)
        self.panel_right.SetSizerAndFit(self.grid_right)
        self.Center()
        self.Show()
        print('get',type(self.grid_right.Children[0]))
    def select_unit(self, event):
        self.SelectUnit=event.GetEventObject().GetStringSelection()
        self.Title = self.SelectUnit
        def refresh_att(ctrl_list, attribute_dict):
            ''''''
            selete_unit = self.unit_dict[self.SelectUnit]#选择的英雄的属性字典
            for i in ctrl_list:
                # 属性中文名
                str1 = i.StaticText.GetLabelText()
                # 属性英文名
                try:
                    str2 = attribute_dict[str1]
                    print('属性',str1,str2)
                except KeyError:
                    print('错误,跳过  str1 =', str1)
                    str3 = self.error_str[0]
                    next
                except:
                    print('错误')
                # 属性值
                try:
                    str3 = selete_unit[str2]
                except KeyError:
                    str3 = self.error_str[0]
                except:
                    str3 = self.error_str[1]
                # 属性值赋给文本框
                ctrl_list[ctrl_list.index(i)].TextCtrl.SetLabel(str3)
        ##############################################
        refresh_att(self.CtrlList1.clist, 公共变量.attribute_name_dict)
        
        # 显示英雄主属性
        self.AttributePrimary.clist[0].TextCtrl.SetLabel(
            self.unit_dict[self.SelectUnit]["AttributePrimary"])
        # 显示 攻击类型(近战\远程)
        self.AttackCapabilities.clist[0].TextCtrl.SetLabel(
            self.unit_dict[self.SelectUnit]["AttackCapabilities"])
        # 显示 英雄技能
        for i in self.skill.clist:
            n = self.skill.clist.index(i)
            self.skill.clist[n].TextCtrl.SetLabel(self.unit_dict[self.SelectUnit][
                公共变量.skill_dict[i.StaticText.GetLabelText()]])
        # 显示 英雄天赋技能
        for i in self.special_bonus.clist:
            n = self.special_bonus.clist.index(i)
            self.special_bonus.clist[n].TextCtrl.SetLabel(self.unit_dict[self.SelectUnit][
                公共变量.special_bonus_dict[i.StaticText.GetLabelText()]])
        print(self.special_bonus.clist[0].StaticText.GetLabelText())
        #secondChoice.SetItems(newItems)
        #Choice(parent, id=ID_ANY,  choices=[])

    def check_readData(self, Event):
        '''点击 读取数据按钮 时发生的事件'''
        self.unit_dict = GUI函数.readData()
        self.unit_name_list = list(self.unit_dict.keys())
        print(self.unit_name_list)
        self.unit_name_list_box.Items = self.unit_name_list

    def add_ctrl(self, grid, panel):
        '''在右侧窗口添加控件以显示属性'''
        # 添加显示基础属性的控件
        l = 公共变量.attribute_name_dict
        self.CtrlList1=CtrlList(panel,grid,(1,0),n=len(l))
        for i in range(len(l)):
            self.CtrlList1.clist[i].StaticText.SetLabel(list(l.keys())[i])
        # 显示英雄主属性
        self.AttributePrimary=CtrlList(panel,grid,(1,2),n=1,IsHasChoice=True,ChoiceList=公共变量.ChoiceItems_list_AttributePrimary)
        self.AttributePrimary.clist[0].Choice.Selection=0
        self.AttributePrimary.clist[0].StaticText.SetLabel('英雄主属性')
        # 显示 攻击类型(近战\远程)
        self.AttackCapabilities=CtrlList(panel,grid,(3,2),n=1,IsHasChoice=True,ChoiceList=公共变量.ChoiceItems_list_AttackCapabilities)
        self.AttackCapabilities.clist[0].Choice.Selection=0
        self.AttackCapabilities.clist[0].StaticText.SetLabel('攻击类型')
        # 显示 英雄技能
        self.skill=CtrlList(panel,grid,(5,2),n=6,IsHasChoice=True,ChoiceList=公共变量.ChoiceItems_list_skill)
        self.skill.clist[0].Choice.Selection=0
        for i in self.skill.clist:
            n = self.skill.clist.index(i)
            self.skill.clist[n].StaticText.SetLabel(list(公共变量.skill_dict.keys())[n])
            self.skill.clist[n].Choice.Selection=0
        # 显示 英雄天赋技能
        self.special_bonus=CtrlList(panel,grid,(12,2),n=8,IsHasChoice=True,
            width=200,ChoiceList=公共变量.ChoiceItems_list_special_bonus)
        self.special_bonus.clist[0].Choice.Selection=0
        for i in self.special_bonus.clist:
            n = self.special_bonus.clist.index(i)
            self.special_bonus.clist[n].StaticText.SetLabel(list(公共变量.special_bonus_dict.keys())[n])
            self.special_bonus.clist[n].Choice.Selection=0
        #############################################################


def 启动窗口():
    app = wx.App()
    Mywin()
    app.MainLoop()


启动窗口()