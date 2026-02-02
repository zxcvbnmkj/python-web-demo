# 1，这个文件展示了，如何获取下拉框中用户选择的值。
# 用户可在下拉框选一个值，点击按钮，会打印出当前下拉框的值
# 2，该文件很好的体现了gr.State的用法。以及什么时候需要用它，它其实就是一个全局变量。它可由应用中的所有组件共享状态。
# 用它相当于用python的全局变量
import gradio as gr

MYMODE = ["RAG", "faa"]
with gr.Blocks() as demo:
    # (1)定义组件
    mymode = gr.Dropdown(
        label="选择模式", choices=MYMODE, multiselect=False, value=MYMODE[0], interactive=True,
        show_label=True, container=False, elem_id="model-select-dropdown", filterable=False
    )
    the_global_mode = gr.State(123456789)
    greet_btn = gr.Button("printMODE")


    # 定义事件函数
    def get_mode(mymode):
        the_global_mode = mymode
        return the_global_mode


    def print_mode(the_global_mode):
        print(the_global_mode)


    # 绑定组件和事件。即当某个组件发生什么变化时，调用哪个函数
    mymode.change(get_mode, inputs=mymode, outputs=the_global_mode)
    greet_btn.click(fn=print_mode, inputs=the_global_mode)

demo.launch()
