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
#全局变量######################
#公共变量.currentline=0      #向grid添加控件时当前所在的行号
########################
class LineCtrls(object):
    '''创建创造一个控件对象,包括:\n
        StaticText:显示属性名称\n
        TextCtrl:显示属性值\n
        wx.Choice:从选择项中选择属性值\n
        key_cn:属性名(中文)\n
        key_eng():属性名(英文)\n
        value_cn:属性值(中文)\n
        value_eng:属性值(英文)'''
    def __init__(self, panel, width,mylabel='',myitems=[],unit_dict={}):
        '''构造函数,创造一组控件,包括2个标签和2个文本框 \n
        mylabel : 标签中的文字列表 \n
        myitems : choices的选择项列表\n
        panel=wx.Panel()\n
        selete_unit : 当前选择的单位'''
        # 创建一个标签,坐标(n,0)
        self.StaticText = wx.StaticText(panel, label=mylabel,style=wx.ALIGN_RIGHT)
        self.StaticText.SetBackgroundColour('white') #背景色
        self.TextCtrl=wx.TextCtrl(panel,size=(width,-1),style=wx.TE_RIGHT)
        self.Choice = wx.Choice(panel,choices=myitems)
        #key
        self.key_cn=mylabel
        self.selete_unit={}
    def key_eng(self):
        '''根据属性值中文获取属性值(英文).\n'''
        value=''
        try:
            value = 公共变量.translation[self.key_cn]
            #print('属性',self.key_cn,value)
        except KeyError:
            print('错误,找不到key,跳过  self.key_cn =', self.key_cn)
            value =公共变量.str_null
        except:
            print('其他错误')
        #value='ArmorPhysical'##############test
        return value
    def value_eng(self):
        '''根据 属性名(key_eng()) 获取属性值,值为英文.\n
            selete_unit:表示一个单位的字典,内容形式为:\n
            { key1 : value1 , key2 : value2 , ... , keyn : valuen }
        '''
        value = ''
        try:
            value = self.selete_unit[self.key_eng()]
        except KeyError:
            value = 公共变量.str_null
        except:
            value = 公共变量.str_error
        return value
    def value_cn(self):
        '''根据属性值(英文)获取属性值(中文).\n
            '''
        rv=''
        try:
            rv = 公共变量.translation[self.value_eng()]
            #print('属性',self.value_eng(),rv)
        except KeyError:
            print('错误,找不到key  self.value_eng =', self.value_eng())
            rv =self.value_eng()
        except:
            print('其他错误')
        return rv


class ctrls(object):
    '''创造一组控件,第1行为1个 StaticText ,作为标题,用于显示一类属性的名称.\n
        其余每行为一组 LineCtrls 控件,每个 LineCtrls 控件包含三个控件:\n
        StaticText : 显示属性名称\n
        TextCtrl :显示属性值 \n
        Choice  :可不显示,用于更改属性值
    '''
    def __init__(self,panel,grid,class_str,colunm=0,IsHasChoice=True ,width=100):
        '''n: CtrlList包含的控件个数
        IsTextCtrl : 要TextCtrl还是Choic,默认TextCtrl
        '''
        #global 公共变量.currentline
        self.head=wx.StaticText(panel,label=class_str, style=wx.ALIGN_CENTER)
        self.linectrlslist=[]
        try:
            l = 公共变量.attribute_dict[class_str]
            print('l= ',l)
        except :
            l=[]
            print('问题语句','l = 公共变量.attribute_dict[class_str]')
        try:
            myitem=公共变量.choiceitems_dict[class_str]
            print('myitem = ',myitem)
        except :
            myitem=[]
            print('问题语句','myitem=公共变量.choiceitems_dict[class_str]')
        for i in l:
            self.linectrlslist.append(LineCtrls(panel,width,mylabel=i,myitems=myitem))
        公共变量.currentline=公共变量.currentline+1
        if IsHasChoice:
            grid.Add(self.head,pos=(公共变量.currentline,colunm),flag= wx.ALIGN_CENTER)
            try:
                self.linectrlslist[0].TextCtrl.Size=(500,-1)
            except:
                pass
            for i in self.linectrlslist:
                x=self.linectrlslist.index(i)+1+公共变量.currentline
                grid.Add(i.StaticText,pos=(x,colunm),flag= wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)
                self.linectrlslist[self.linectrlslist.index(i)].TextCtrl.Size=(500,-1)
                print(i.TextCtrl.Size)
                grid.Add(i.TextCtrl  ,pos=(x,colunm+1),flag=  wx.ALIGN_CENTER)
                grid.Add(i.Choice    ,pos=(x,colunm+2),flag= wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)
            公共变量.currentline = 公共变量.currentline + len(self.linectrlslist) + 1
        else:
            grid.Add(self.head,pos=(公共变量.currentline,colunm),flag= wx.ALIGN_CENTER )
            for i in self.linectrlslist:
                x=self.linectrlslist.index(i)+1+公共变量.currentline
                grid.Add(i.StaticText,pos=(x,colunm),flag= wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)
                grid.Add(i.TextCtrl  ,pos=(x,colunm+1))#,flag= wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)
            公共变量.currentline = 公共变量.currentline + len(self.linectrlslist) + 1


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
            None, title='Dota2 游戏数据修改', size=(800, 700))
        ################################################################
        #对象的属性#
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
        self.读取数据.Bind(wx.EVT_BUTTON, self.check_readdata)
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
        def refresh_att(linectrlslist):
            #i = linectrlslist[0]
            for i in linectrlslist: # type(i) = linectrls
                i.selete_unit=self.unit_dict[self.SelectUnit]#选择的英雄的属性字典
                print(i.key_cn,i.value_eng())
                linectrlslist[linectrlslist.index(i)].TextCtrl.SetLabel(i.value_cn())
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
        print(self.unit_name_list)
        self.unit_name_list_box.Items = self.unit_name_list

    def check_savedata(self, Event):
        '''点击 保存数据按钮 时发生的事件'''

        for i in self.leftctrls:
            for j in i.linectrlslist:
                self.unit_dict[self.SelectUnit][j.key_eng()]=j.TextCtrl.GetLabelText()
        for i in self.midctrls:
            for j in i.linectrlslist:
                self.unit_dict[self.SelectUnit][j.key_eng()]=j.TextCtrl.GetLabelText()
        for i in self.rightctrls:
            for j in i.linectrlslist:
                temp = j.Choice.GetStringSelection()
                if  temp !='':
                    try:
                        temp=公共变量.translation[temp]
                        self.unit_dict[self.SelectUnit][j.key_eng()]=temp
                    except:
                        print('check_savedata 错误, 公共变量.translation 无',temp)
        GUI函数.saveData(self.unit_dict)

    def add_ctrl(self, grid, panel):
        '''在右侧窗口添加控件以显示属性'''
        n=6#左侧属性类别数量
        ############################################################
        # self.leftctrls是一个列表,元素类型为:ctrls, 
        公共变量.currentline=0
        leftattribute=list(公共变量.attribute_dict.keys())[:3]#['护甲','攻击']
        self.leftctrls=[]
        for i in leftattribute:
            self.leftctrls.append(ctrls(panel,grid,i,0,False,width=75))
        
        #######################################################
        公共变量.currentline=0
        midtattribute=list(公共变量.attribute_dict.keys())[3:6]   #['技能']
        self.midctrls=[]
        for i in midtattribute:
            self.midctrls.append(ctrls(panel,grid,i,2,False,width=75))
        #######################################################
        公共变量.currentline=0
        rightattribute=list(公共变量.attribute_dict.keys())[-4:]   #['技能']
        self.rightctrls=[]
        for i in rightattribute:
            self.rightctrls.append(ctrls(panel,grid,i,4,width=120))
        ########################################################
        # 添加保存按钮
        self.保存数据 = wx.Button(panel, label="保存数据",pos=(22,0))
        print(公共变量.currentline)
        grid.Add(self.保存数据,pos=(公共变量.currentline,2),flag= wx.ALIGN_CENTER)
        self.保存数据.Bind(wx.EVT_BUTTON, self.check_savedata)


def 启动窗口():
    app = wx.App()
    win=Mywin()
    app.MainLoop()


启动窗口()

