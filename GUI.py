'''用于创建一个人窗口程序,必须使用 GUI函数.py'''
import wx
import GUI函数
#wx.Choice(parent, id, pos, size, n, choices[], style) 
class creatCtrl(object):
    '''创建创造一组控件'''
    def event(self,event): 
        '''绑定事件,用于在标签中显示文字'''
        mystr1=self.valueText1.GetString()
        self.label1.SetLabel(mystr1) 
        mystr2=self.valueText2.GetString()
        self.label2.SetLabel(mystr2) 
    def __init__(self,labelstr_list,linenumber=0,app=wx.App(),grid=wx.GridBagSizer(0,0),panel=wx.Panel()):
        '''构造函数,创造一组控件,包括2个标签和2个文本框 \n
        namestr:标签中的文字
        linenumber : 行号
        app=wx.App(),grid=wx.GridBagSizer(0,0),panel=wx.Panel()'''
        #创建一个标签,坐标(n,0)
        self.label1=wx.StaticText(panel,label=labelstr_list[0],style = wx.ALIGN_CENTRE)
        grid.Add(self.label1,pos=(linenumber,0),flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALL) 
        #创建一个文本框,坐标(n,1)
        self.valueText1=wx.TextCtrl(panel)
        grid.Add(self.valueText1,pos=(linenumber,1)) 
        #创建第二个标签,坐标(n,2)
        self.label2=wx.StaticText(panel,label=labelstr_list[1],style = wx.ALIGN_CENTRE)
        grid.Add(self.label2,pos=(linenumber,2),flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALL) 
        #创建第二个文本框,坐标(n,3)
        self.valueText2=wx.TextCtrl(panel)
        grid.Add(self.valueText2,pos=(linenumber,3)) 
        #
        #事件绑定
        self.valueText1.Bind(wx.EVT_TEXT, self.event)

class creatLabel(object):
    def __init__(self,namestr,pos,app=wx.App(),grid=wx.GridBagSizer(0,0),panel=wx.Panel()):
        self.label=wx.StaticText(panel,label=namestr,style = wx.ALIGN_CENTRE)
        grid.Add(self.label,pos,flag=wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL) 

unitNameList=['unit1','unit2']

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
        super(Mywin, self).__init__(None, title ='Dota2 游戏数据修改',size=(500,650)) 
        ################################################################
        #对象的属性#
        self.unit_dict={}
        self.unit_list=[]
        self.attribute_list=[
            #["修改对象","单位类型"],
            ['物理护甲','魔法护甲'],
            ['最小攻击力','最大攻击力'],
            ['攻击类型','攻击速度'],
            ['攻击距离','弹道速度'],
            ['移动','移动速度'],
            ['生命值','生命恢复速度'],
            ['魔法值','魔法恢复速度'],
            ['白天视野','夜间视野']
        ]
        ################################################################
        #分离器对象添加到顶层帧。
        splitter = wx.SplitterWindow(self, -1) #一个布局管理器，拥有两个子窗口,子窗口大小可以通过拖动它们之间的界限来动态变化。
        #左侧窗口###################################################
        self.panel_right = wx.Panel(splitter, -1) 
        self.grid_left = wx.BoxSizer(wx.VERTICAL) #左侧的窗口,用于显示 单位名称
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
        #左侧窗口添加内容
        self.读取数据 = wx.Button(self.panel_right, label = "读取数据" ) 
        self.grid_left.Add(self.读取数据,0) 
        self.label_=wx.StaticText(self.panel_right,label='',style = wx.ALIGN_CENTER)
        self.grid_left.Add(self.label_,0) 
        self.unitlabel=wx.StaticText(self.panel_right,label='选择单位')
        self.grid_left.Add(self.unitlabel,0) 
        self.unit_list_box = wx.ListBox(self.panel_right, choices = self.unit_list, style = wx.LB_SINGLE) 
        self.grid_left.Add(self.unit_list_box,90) 
        #绑定数据
        self.读取数据.Bind(wx.EVT_BUTTON, self.check_readData)
        self.Bind(wx.EVT_LISTBOX, self.select_unit, self.unit_list_box ) #绑定,点击左侧选择项时发生事件
        #右侧窗口###################################################
        grid_right = wx.GridBagSizer(0,0) #右侧布局控件,其它控件将放在其内,用于单位显示属性
        panel_right = wx.Panel(splitter, -1) 
        #右侧窗口添加内容
        self.add_ctrl(grid_right,panel_right)
        ###########################################################
        #self.Show()
        splitter.SplitVertically(self.panel_right, panel_right) 
        #self.panel_right.SetSizer(self.grid_left) 
        self.panel_right.SetSizerAndFit(self.grid_left)
        panel_right.SetSizerAndFit(grid_right)
        #panel_right.SetSizer(_right) 
        #self.Centre() 
        self.Show()
    def select_unit(self, event): 
        select_unit=event.GetEventObject().GetStringSelection()
        self.Title=event.GetEventObject().GetStringSelection()
        att=''
        for i in self.attribute_list:
            for j in i:
                print(self.unit_dict[select_unit][j])

        pass
    def check_readData(self,Event):
        self.unit_dict = GUI函数.readData()
        self.unit_list = list(self.unit_dict.keys())
        print(self.unit_list)
        self.unit_list_box.Items=self.unit_list

    def OnChoice(self,event): 
      self.label.SetLabel("正在修改 "+ self.choice.GetString
         (self.choice.GetSelection())) 
    def sizeChange(self,event):
       print(self.GetSizes())
       self.label.SetLabel(self.GetSizes()) 
    def add_ctrl(self,grid,panel):
        '''在右侧窗口添加控件以显示属性'''
        ctrl_list=[]
        for i in self.attribute_list:
            ctrl_list.append(creatCtrl(i,self.attribute_list.index(i),self,grid,panel))
        #最后一行###################################################
        self.保存 = wx.Button(panel, label = "保存") 
        self.重置 = wx.Button(panel, label = "重置") 
        grid.Add(self.保存, pos = (len(self.attribute_list), 3),flag = wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, border = 3) 
        grid.Add(self.重置, pos = (len(self.attribute_list), 2),flag = wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, border = 3) 
        #GUI函数在GUI函数.py文件中
        #self.choice.Bind(wx.EVT_CHOICE, self.OnChoice)
        self.保存.Bind(wx.EVT_BUTTON, GUI函数.saveData)
        self.重置.Bind(wx.EVT_BUTTON, GUI函数.resetData)
        

def 启动窗口():
    app = wx.App() 
    Mywin() 
    app.MainLoop()

启动窗口()