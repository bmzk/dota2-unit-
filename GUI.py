'''用于创建一个人窗口程序,必须使用 GUI函数.py'''

import wx


import GUI函数
import 公共变量


# wx.Choice(parent, id, pos, size, n, choices[], style)
class creatCtrl(object):
    '''创建创造一组控件'''
    def __init__(self, labelstr, pos_x, pos_y=0,
                 app=wx.App(), grid=wx.GridBagSizer(0, 0), panel=wx.Panel(), ctrl_width=100):
        '''构造函数,创造一组控件,包括2个标签和2个文本框 \n
        namestr:标签中的文字
        linenumber : 行号
        app=wx.App(),grid=wx.GridBagSizer(0,0),panel=wx.Panel()'''
        # 创建一个标签,坐标(n,0)
        self.label1 = wx.StaticText(
            panel, label=labelstr, size=(100, -1), style=wx.ALIGN_RIGHT)
        self.label1.Wrap(200)
        self.label1.SetBackgroundColour('white')
        #wx.StaticText.SetBackgroundColour()
        # self.label1.GetLabelText
        grid.Add(self.label1, pos=(pos_x, pos_y),
                 flag=wx.EXPAND | wx.ALIGN_LEFT | wx.ALL)
        # 创建一个文本框,坐标(n,1)
        self.valueText1 = wx.TextCtrl(panel, size=(ctrl_width, -1))
        grid.Add(self.valueText1, pos=(pos_x, pos_y+1))
        # #创建第二个标签,坐标(n,2)
        # self.label2=wx.StaticText(panel,label=labelstr_list[1],style = wx.ALIGN_CENTRE)
        # grid.Add(self.label2,pos=(linenumber,2),flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALL)
        # #创建第二个文本框,坐标(n,3)
        # self.valueText2=wx.TextCtrl(panel)
        # grid.Add(self.valueText2,pos=(linenumber,3))
        #
class StaticText_Ctrls(object):
    '''创建创造一列StaticText控件'''
    def __init__(self, StaticText_str:list,clunm=0, width=100,app=wx.App(), 
        grid=wx.GridBagSizer(0, 0), panel=wx.Panel(),IsStartFromLine0=False):
        '''构造函数,创造一组控件,包括2个标签和2个文本框 \n
        StaticText_str:标签中的文字列表
        app=wx.App(),grid=wx.GridBagSizer(0,0),panel=wx.Panel()'''
        self.StaticText_Ctrl_list=[]
        # 创建一个标签,坐标(n,0)
        for i in StaticText_str:
            StaticText = wx.StaticText(panel, label=i, size=(width, -1),style=wx.ALIGN_RIGHT)
            StaticText.Wrap(200)
            StaticText.SetBackgroundColour('white')
            self.StaticText_Ctrl_list.append(StaticText)
        for i in self.StaticText_Ctrl_list:
            if IsStartFromLine0:
                grid.Add(i, pos=(self.StaticText_Ctrl_list.index(i)+1, clunm),
                    flag=wx.EXPAND | wx.ALIGN_LEFT | wx.ALL)
            else:
                grid.Add(i, pos=(self.StaticText_Ctrl_list.index(i), clunm),
                    flag=wx.EXPAND | wx.ALIGN_LEFT | wx.ALL)



class creatLabel(object):
    def __init__(self, namestr, pos, app=wx.App(), grid=wx.GridBagSizer(0, 0), panel=wx.Panel()):
        self.label = wx.StaticText(panel, label=namestr, style=wx.ALIGN_CENTRE)
        grid.Add(self.label, pos, flag=wx.EXPAND |
                 wx.ALIGN_CENTER_HORIZONTAL | wx.ALL)


unitNameList = ['unit1', 'unit2']


class Mywin(wx.Frame):
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
        self.error_str1 = '无此键值'  # 读取属性时出现不存在的属性显示键值
        self.error_str2 = '错误键值'
        self.unit_dict = {}
        self.unit_name_list = []
        self.ctrl_list = []
        self.skill_ctrl_list = []
        ################################################################
        # 分离器对象添加到顶层帧。
        # 一个布局管理器，拥有两个子窗口,子窗口大小可以通过拖动它们之间的界限来动态变化。
        splitter = wx.SplitterWindow(self, -1)
        #左侧窗口###################################################
        self.panel_right = wx.Panel(splitter, -1)
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
        self.读取数据 = wx.Button(self.panel_right, label="读取数据")
        self.grid_left.Add(self.读取数据, 0)
        self.label_ = wx.StaticText(
            self.panel_right, label='', style=wx.ALIGN_CENTER)
        self.grid_left.Add(self.label_, 0)
        self.unitlabel = wx.StaticText(self.panel_right, label='选择单位')
        self.grid_left.Add(self.unitlabel, 0)
        self.unit_name_list_box = wx.ListBox(
            self.panel_right, choices=self.unit_name_list, style=wx.LB_SINGLE)
        self.grid_left.Add(self.unit_name_list_box, 90)
        # 绑定数据
        self.读取数据.Bind(wx.EVT_BUTTON, self.check_readData)
        self.Bind(wx.EVT_LISTBOX, self.select_unit,
                  self.unit_name_list_box)  # 绑定,点击左侧选择项时发生事件
        #右侧窗口###################################################
        grid_right = wx.GridBagSizer(0, 0)  # 右侧布局控件,其它控件将放在其内,用于单位显示属性
        panel_right = wx.Panel(splitter, -1)
        # 右侧窗口添加内容
        self.add_ctrl(grid_right, panel_right)
        ###########################################################
        # self.Show()
        splitter.SplitVertically(self.panel_right, panel_right)
        # self.panel_right.SetSizer(self.grid_left)
        self.panel_right.SetSizerAndFit(self.grid_left)
        panel_right.SetSizerAndFit(grid_right)
        # panel_right.SetSizer(_right)
        # self.Centre()
        self.Show()

    def select_unit(self, event):
        def read_att(ctrl_list, attribute_dict):
            ''''''
            select_unit_str = event.GetEventObject().GetStringSelection()
            selete_unit = self.unit_dict[select_unit_str]
            for i in ctrl_list:
                # 属性中文名
                str1 = i.label1.GetLabelText()
                # 属性英文名
                try:
                    str2 = attribute_dict[str1]
                except KeyError:
                    print('错误,跳过  str1 =', str1)
                    str3 = self.error_str1
                    next
                except:
                    print('错误')
                # 属性值
                #str3 = selete_unit[str2]
                try:
                    str3 = selete_unit[str2]
                except KeyError:
                    str3 = self.error_str1
                except:
                    str3 = self.error_str2
                # 属性值赋给文本框
                ctrl_list[ctrl_list.index(i)].valueText1.SetLabel(str3)
        self.Title = event.GetEventObject().GetStringSelection()
        read_att(self.ctrl_list, 公共变量.attribute_name_dict)
        read_att(self.skill_ctrl_list, 公共变量.skill_dict)

    def check_readData(self, Event):
        self.unit_dict = GUI函数.readData()
        self.unit_name_list = list(self.unit_dict.keys())
        print(self.unit_name_list)
        self.unit_name_list_box.Items = self.unit_name_list

    def add_ctrl(self, grid, panel):
        '''在右侧窗口添加控件以显示属性'''
        l = 公共变量.attribute_name_dict
        # 控件所在行号
        n = 1
        for i in l:
            self.ctrl_list.append(creatCtrl(i, n, 0, self, grid, panel))
            n = n+1
        #最后一行###################################################
        self.保存 = wx.Button(panel, label="保存")
        self.重置 = wx.Button(panel, label="重置")
        grid.Add(self.保存, pos=(n+1, 1), flag=wx.ALL |
                 wx.ALIGN_CENTER_HORIZONTAL, border=3)
        grid.Add(self.重置, pos=(n+1, 0), flag=wx.ALL |
                 wx.ALIGN_CENTER_HORIZONTAL, border=3)
        # GUI函数在GUI函数.py文件中
        #self.choice.Bind(wx.EVT_CHOICE, self.OnChoice)
        self.保存.Bind(wx.EVT_BUTTON, GUI函数.saveData)
        self.重置.Bind(wx.EVT_BUTTON, GUI函数.resetData)
        #技能列#############################################
        m = 1
        for i in 公共变量.skill_dict:
            self.skill_ctrl_list.append(
                creatCtrl(i, m, 2, self, grid, panel, ctrl_width=200))
            m = m+1
        st=StaticText_Ctrls(['a','b','c','d'],4,100,self,grid,panel)

def 启动窗口():
    app = wx.App()
    Mywin()
    app.MainLoop()
