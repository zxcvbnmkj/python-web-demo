from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

"""
输入
http://127.0.0.1:8000/items/
输出的值是默认的0和10

输入http://127.0.0.1:8000/items/?skip=1&limit=5
这样传参

不可写作http://127.0.0.1:8000/items/?1&5。是错误的
http://127.0.0.1:8000/items/?aaa=1&fsw=5也是错误的。


这是 /items/ 路由接受了两个参数（这也是get请求），而不是2.py那样的【路径参数】，把参数直接放在路径上面
"""