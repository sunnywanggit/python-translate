from tkinter import *
from tkinter import messagebox
import requests

# 完成翻译功能  定义translate函数，并爬取有道翻译结果
# 1 获取用户输入内容
# 2 爬取有道翻译结果
# 3 将翻译结果进行显示

def translate():
    # 获取需要被翻译的内容
    content = entryWord.get()
    # 清除多余的空格
    content = content.strip()
    if content == '':
        messagebox.showinfo('提示',message='输入内容不能为空')
    else:
        url= 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        data={}
        data['i'] = content
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        # data['salt'] = '15946601399405'
        # data['sign'] = '442032ec89f135fa9c4c3a0f006fe5d4'
        # data['ts'] = '1594660139940'
        # data['bv'] = '02a6ad4308a3443b3732d855273259bf'
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CLICKBUTTION'

        response= requests.post(url,data=data)
        result = response.json()
        trans = result['translateResult'][0][0]['tgt']
        # 设置显示到输出框
        output.set(trans)
        return  trans



# 创建图形化界面：交互窗口
window = Tk()

# 前两个参数调整窗口大小 最后两个参数确定坐标
window.geometry('300x100+500+300')

#窗口的标题
window.title('中英互译')

#控件
label = Label(window,text = '输入要翻译的文字:',font=('微软雅黑',10))

#明确控件的位置 使用网格式布局
label.grid()

# 输入框
entryWord = Entry(window,font=('微软雅黑',10),fg='red')

#明确控件的位置 使用网格式布局
entryWord.grid(row=0,column=1)

label1 = Label(window,text = '翻译之后的结果是:',font=('微软雅黑',10))
label1.grid(row=1,column=0)

output = StringVar()

entry1  = Entry(window,font=('微软雅黑',10),fg='red',textvariable=output)
entry1.grid(row=1,column=1)

buttonTranslate = Button(window,text='翻译',width=10,command = translate)
buttonTranslate.grid(row=2,column=0)

buttonExit = Button(window,text='退出',width=10,command = window.quit)
# sticky 对齐方式
buttonExit.grid(row=2,column=1,sticky=E)

# mainloop 消息循环 在这里的作用就是显示窗口
window.mainloop()


