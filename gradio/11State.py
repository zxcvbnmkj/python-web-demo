import gradio as gr
mode=gr.State("RAG模式")
#<gradio.components.state.State object at 0x000001AD01F46260>
print(mode)
#RAG模式
print(mode.value)
if mode.value=="RAG模式":
    print("aaa")
else:
    print("bbb")




"""
若要在定义的表示“事件”的函数中，使用State变量。必须通过“组件+事件”代码把State变量作为输入，传入到函数中。这样print该State变量，出现的是值。
如果某个函数的实参不包括该State变量，函数内部却引用了，print该变量出现的是变量地址。需要State.value才会出现值。且函数必须是“组件+事件”代码中引用了的函数，实参也必须通过“组件+事件”代码传入才有用
"""
def test(mode):
    print(mode)
test(mode)