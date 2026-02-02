import gradio as gr


def greet(name):
    return "Hello " + name + "!"


with gr.Blocks() as demo:
    """
    1. 以下三个赋值语句，都会在应用中显示出组件
    2. Block不能像Interface一样，自动用形参为text组件命名，也不能直接使用“text”,而是需要实例化Textbox类
    """
    # 设置输入组件
    name = gr.Textbox(label="Name")
    # 设置输出组件.interactive=True使得输出组件中的内容可编辑
    output = gr.Textbox(label="Output Box", interactive=True)
    # 设置按钮
    greet_btn = gr.Button("Greet")
    # 设置按钮点击事件
    greet_btn.click(fn=greet, inputs=name, outputs=output)

demo.launch()
