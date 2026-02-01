from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

#因为item_id是个变量，因此网址需要写作/items/字符串。或者/items/任意变量名=字符串
#app.get这里规定了是get请求
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

"""
输入 http://127.0.0.1:8000/items/一个数字
如http://127.0.0.1:8000/items/5
会得到
{
    "item_id": 5,
    "q": null
}
输入http://127.0.0.1:8000/items/5?q=hahaha
或者http://127.0.0.1:8000/items/5?aaaa（任意）=hahaha
或者http://127.0.0.1:8000/items/5?hahaha

！！！但是一般都写作q=hahaha，函数形参是什么，路径就写什么
输出
{
    "item_id": 5,
    "q": "hahaha"
}
"""
"""
输入（Swagger UI风格）
http://127.0.0.1:8000/docs
就可以看到自动生成的API文档了，里面介绍了各个路径的作用

或者http://127.0.0.1:8000/redoc
（ReDoc 风格）
"""