#通过pip install gradio安装该库。这个库常简称为gr。
import gradio as gr

#将为输入组件中的text上面标注"name"，slider组件标注intensity。获取输入后，在输出组件中显示："Hello " * intensity + name + "!"
def greet(name, intensity):
    return "Hello " * intensity + name + "!"

#通过Interface类创建gradio应用的实例
demo = gr.Interface(
    #要调用的函数
    fn=greet,
    #输入组件自带“clear”、"submit"两个按钮
    #应用将有两个输入控件：文本框 ("text") 和一个滑块 ("slider")
    inputs=["text", "slider"],
    #自带flag按钮。Flag按钮用于保存结果到本地。在同级目录下，自动创建flagged文件，存储了结果。
    #加入参数 allow_flagging="never",可不显示该按钮
    #用一个文本框显示输出
    outputs=["text"],
    allow_flagging="never"
)
#运行实例
#inbrowser=True表示自动打开网址
demo.launch(inbrowser=True)
