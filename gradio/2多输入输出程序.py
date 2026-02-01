import gradio as gr

#输入列表中的每个组件按顺序对应于函数的一个参数。输出列表中的每个组件按顺序排列对应于函数返回的一个值。
#对于输入组件，会使用函数的形参名字作为组件名字，显示在应用中。
#该函数有3个输入参数和2个输出参数
def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


demo = gr.Interface(
    fn=greet,
    #按照处理程序设置输入组件
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    #按照处理程序设置输出组件
    outputs=["text", "number"],
)
demo.launch()