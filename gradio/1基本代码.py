import gradio as gr

# 将为输入组件中的 text 上面标注"name"，slider 组件标注 intensity
# 获取输入后，在输出组件中显示："Hello " * intensity + name + "!"
def greet(name, intensity):
    return "Hello " * intensity + name + "!"

demo = gr.Interface(
    fn=greet,
    # 输入组件自带“clear”、"submit"两个按钮
    # 应用将有两个输入控件：文本框 ("text") 和一个滑块 ("slider")
    inputs=["text", "slider"],
    # 自带 flag 按钮用于保存结果到本地。在同级目录下，自动创建 flagged 文件存储结果
    # 加入参数 allow_flagging="never",可不显示该按钮
    # 用一个文本框显示输出
    outputs=["text"],
    allow_flagging="never"
)

# inbrowser=True 自动打开网址
demo.launch(inbrowser=True)
