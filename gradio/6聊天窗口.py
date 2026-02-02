import random
import gradio as gr


def chat(message, history):
    history = history or []
    message = message.lower()
    if message.startswith("how many"):
        response = random.randint(1, 10)
    elif message.startswith("how"):
        response = random.choice(["## Great\nAA", "Good<br>HHH", "Okay\nFW", "<h1>Bad<br>QS"])
    elif message.startswith("where"):
        response = random.choice(["Here", "There", "Somewhere"])
    else:
        response = "I don't know"
    history.append((message, response))
    return history, history


# 设置一个对话窗。作为输出显示。
chatbot = gr.Chatbot()

# gr.state是一个保持当前状态的组件。在后台存储一些变量方便访问和交互。【临时变量】
# 当用户刷新页面时，State 变量的值被清除
# 用法：num = gr.State(value=0)。将参数保持在num中，作为临时变量
demo = gr.Interface(
    chat,
    # 添加state组件
    ["text", "state"],
    [chatbot, "state"],
    # 设置没有保存数据的按钮
    allow_flagging="never",
)
demo.launch()
