import gradio as gr


# 一个简单计算器，含实例说明
def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            # 设置报错弹窗
            raise gr.Error("Cannot divide by zero!")
        return num1 / num2


demo = gr.Interface(
    calculator,
    # 设置输入
    [
        "number",
        gr.Radio(["add", "subtract", "multiply", "divide"]),
        "number"
    ],
    # 设置输出
    "number",
    # 显示一个表格，表格题目为examples
    examples=[
        [5, "add", 3],
        [4, "divide", 2],
        [-4, "multiply", 2.5],
        [0, "subtract", 1.2],
    ],
    # 设置网页标题
    title="Toy Calculator",
    # 左上角的描述文字
    description="Here's a sample toy calculator. Enjoy!",
    # 左下角的文字
    article="Check out the examples",
)
demo.launch()
