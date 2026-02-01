
#运行该代码时，先切换到当前目录下，cd fastAPI示例/1基本程序
#再输入uvicorn 1基本程序:app --reload【uvicorn py文件名:该文件中FastAPI实例对应的变量名字 --reload: 启用自动重载功能，使得代码变更后服务器会自动重启】


#Uvicorn 是由 Starlette 框架的作者编写的 ASGI（Asynchronous Server Gateway Interface） 服务器，
# 旨在提供高性能的异步请求处理能力。它使用 asyncio 库实现异步 I/O 操作，支持 HTTP 和 WebSocket 协议



from fastapi import FastAPI
#创建一个 FastAPI 应用实例
app = FastAPI()

#路由装饰器，将根 URL 路径 (/) 与 read_root 函数关联起来。当用户访问根路径时，FastAPI 会调用这个函数。
@app.get("/")
def read_root():
    return {"Hello": "World"}
#如果返回值是一个字典，网页接受时会自动转换为json



"""
如果不加这个，pycharm中点击运行，因为没有main函数，是什么都不会执行的
只能在Ternimal中输入uvicorn 1基本程序:app --reload
写了以下代码就可以直接点运行，或者python 1基本程序.py
"""
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="1基本程序:app", host="127.0.0.1", port=8000, reload=True)