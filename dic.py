#coding:utf-8
import urllib,urllib.request  
import  tkinter #导入TKinter模块  
from tkinter import scrolledtext
from tkinter import *
import numpy as np
import tkinter.messagebox
  
ytm=tkinter.Tk() #创建Tk对象  
ytm.title("简易多功能检索词典") #设置窗口标题  
ytm.geometry("300x300") #设置窗口尺寸  
path='牛津简明英汉词典.txt'
menubar=Menu(ytm)
fmenu1=Menu(ytm)
fmenu2=Menu(ytm)
l1=tkinter.Label(ytm,text="在此输入单词",foreground = 'gray') #标签 
def choose1():	
	global path
	path='牛津简明英汉词典.txt' 
	l1["text"]="牛津英语"
	    
def choose2():
    global path
    path='入门日本语辞典.txt'
    l1["text"]="日语入门" 

def choose3():
    global path
    path='中国历代职官辞典.txt'
    l1["text"]="中国古代官职" 	

def click():
    tkinter.messagebox.showinfo('作者', '微博:@花果山林四儿\nqq:1275945658\n版权所有©')			
    
# 如果该菜单时顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。
fmenu1.add_command(label='英汉',command=choose1)
fmenu1.add_command(label='日汉',command=choose2)
fmenu1.add_command(label='*官职',command=choose3,foreground = 'red')
fmenu2.add_command(label='版权信息',command=click)
fmenu2.add_command(label='退出',command=ytm.quit) 
l1.pack() #指定包管理器放置组件  
user_text=tkinter.Entry( background = 'gainsboro') #创建文本框  
user_text.pack()  
text1=scrolledtext.ScrolledText(ytm)
w=tkinter.Label(ytm, text="",foreground = 'red')
menubar.add_cascade(label="词典",menu=fmenu1)
menubar.add_cascade(label="关于",menu=fmenu2)
def getuser():  
    i=0        
    text1.delete(1.0, 'end')
    user=user_text.get() #获取文本框内容  
    with  open(path,'r',encoding='UTF8')as  fp:
        for  line in  fp:
            if  user.strip() in  line:				
                i+=1
                text1.insert('insert',line)    
    w["text"]="检索到%s个词条"%i
    w.pack()         
    text1.pack()
  
tkinter.Button(ytm,bg='yellow',height=1,text="快速查询",command=getuser).pack() #command绑定获取文本框内容方法  
ytm['menu']=menubar
ytm.mainloop() #进入主循环
