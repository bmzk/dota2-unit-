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
currentline1=0      #向grid添加控件时当前所在的行号,第一列
currentline2=0      #向grid添加控件时当前所在的行号,第一列
########################
class LineCtrls(object):
    '''创建创造一个控件对象,包括StaticText \TextCtrl \wx.Choice控件'''
    def __init__(self, panel, mylabel='',myitems=[] ,isspan=False,width=150):
        '''构造函数,创造一组控件,包括2个标签和2个文本框 \n
        mylabel : 标签中的文字列表 \n
        myitems : choices的选择项列表\n
        panel=wx.Panel()'''
        # 创建一个标签,坐标(n,0)
        self.StaticText = wx.StaticText(panel, label=mylabel,style=wx.ALIGN_RIGHT)
        self.StaticText.SetBackgroundColour('white') #背景色
        self.TextCtrl=wx.TextCtrl(panel,size=(width,-1),style=wx.TE_RIGHT)
        self.Choice = wx.Choice(panel,choices=myitems)

class ctrls(object):
    '''创造一组包含1个类别名的StaticText 和 n个StaticText TextCtrl Choice 对象的列表'''
    def __init__(self,panel,grid,class_str,IsHasChoice=True ,width=100):
        '''n: CtrlList包含的控件个数
        IsTextCtrl : 要TextCtrl还是Choic,默认TextCtrl'''
        global currentline1,currentline2
        self.head=wx.StaticText(panel,label=class_str, style=wx.ALIGN_CENTER)
        self.clist=[]
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
            self.clist.append(LineCtrls(panel,mylabel=i,myitems=myitem))
        if IsHasChoice:
            grid.Add(self.head,pos=(currentline2,2),flag= wx.ALIGN_CENTER)
            try:
                self.clist[0].TextCtrl.Size=(500,-1)
            except:
                pass
            for i in self.clist:
                x=self.clist.index(i)+1+currentline2
                grid.Add(i.StaticText,pos=(x,2),flag= wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)
                self.clist[self.clist.index(i)].TextCtrl.Size=(500,-1)
                print(i.TextCtrl.Size)
                grid.Add(i.TextCtrl  ,pos=(x,3),span=(1,2),flag=  wx.ALIGN_CENTER)
                grid.Add(i.Choice    ,pos=(x,6),flag= wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)
            currentline2 = currentline2 + len(self.clist) + 1
        else:
            grid.Add(self.head,pos=(currentline1,0),flag= wx.ALIGN_CENTER )
            for i in self.clist:
                x=self.clist.index(i)+1+currentline1
                grid.Add(i.StaticText,pos=(x,0),flag= wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)
                grid.Add(i.TextCtrl  ,pos=(x,1))#,flag= wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)
            currentline1 = currentline1 + len(self.clist) + 1



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
        self.str_null = '无此键值'  # 读取属性时出现不存在的属性显示键值
        self.str_error = '错误键值' 
        self.unit_dict = {}
        self.unit_name_list = []
        self.ctrl_list = []
        self.skill_ctrl_list = []
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

    def select_unit(self, event):
        self.SelectUnit=event.GetEventObject().GetStringSelection()
        self.Title = self.SelectUnit
        def refresh_att(ctrl_list):
            ''''''
            selete_unit = self.unit_dict[self.SelectUnit]#选择的英雄的属性字典
            for i in ctrl_list:
                # 属性中文名
                str1 = i.StaticText.GetLabelText()
                # 属性英文名
                str2=''
                try:
                    str2 = 公共变量.translation[str1]
                    print('属性',str1,str2)
                except KeyError:
                    print('错误,跳过  str1 =', str1)
                    str3 = self.str_null
                    next
                except:
                    str3 = self.str_error
                    print('错误')
                # 属性值
                str3=''
                try:
                    str3 = selete_unit[str2]
                except KeyError:
                    str3 = self.str_null
                except:
                    str3 = self.str_error
                # 属性值赋给文本框
                str4=''
                try:
                    str4= 公共变量.translation[str3]  # 属性值的中文名
                except:
                    str4 = str3
                ctrl_list[ctrl_list.index(i)].TextCtrl.SetLabel(str4)
        ##############################################
        for i in self.leftctrls:
            refresh_att(i.clist)
        for i in self.rightctrls:
            refresh_att(i.clist)
        #refresh_att(self.CtrlList2.clist, 公共变量.skill_dict)
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
        ############################################################
        leftattribute=list(公共变量.attribute_dict.keys())[:5]#['护甲','攻击']
        self.leftctrls=[]
        for i in leftattribute:
            self.leftctrls.append(ctrls(panel,grid,class_str=i,IsHasChoice=False))

        #######################################################
        rightattribute=list(公共变量.attribute_dict.keys())[-5:]   #['技能']
        self.rightctrls=[]
        for i in rightattribute:
            self.rightctrls.append(ctrls(panel,grid,class_str=i))




def 启动窗口():
    app = wx.App()
    Mywin()
    app.MainLoop()


启动窗口()