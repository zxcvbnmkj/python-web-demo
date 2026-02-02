from fastapi import FastAPI, Request  # 从fastapi库导入FastAPI类和Request类
import gradio as gr  # 导入gradio库，用于创建交互式Web应用界面
import uvicorn  # 导入uvicorn库，用于运行ASGI应用

app = FastAPI()  # 创建一个FastAPI应用实例


# 定义一个函数，用于从请求中获取用户信息
# def get_user(request: Request):
#     print("请求头字段：", request.headers)
#     print("获取到的是",request.headers.get("user"))
#     return request.headers.get("user")  # 从请求头中获取"user"字段的值

def get_user(request: Request):
    return "admin"


# 创建一个Gradio Interface，接受一个文本输入并返回一个带有输入内容的问候语
demo = gr.Interface(lambda s: f"Hello {s}!", "textbox", "textbox")

# 使用gradio的mount_gradio_app函数将Gradio应用挂载到FastAPI应用上
# 挂载点设置为"/demo"，并使用get_user函数作为验证用户身份的依赖函数
app = gr.mount_gradio_app(app, demo, path="/demo", auth_dependency=get_user)

# 如果当前脚本作为主程序运行，则使用uvicorn来运行FastAPI应用
# 在本文件中写uvicorn.run可以省略本文件的名字，直接写FastAPP实例的名字即可
if __name__ == '__main__':
    # uvicorn.run(app)
    uvicorn.run(app="2外部登陆:app", host="127.0.0.1", port=8000, reload=True)

# 根节点http://127.0.0.1:8000是空的，请访问
# http://127.0.0.1:8000/demo
