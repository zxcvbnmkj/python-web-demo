from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
#如果返回值是一个字典，网页接受时会自动转换为json


"""
如果不加这个需终端输入: uvicorn filename:app --reload
添加后: python filename.py
"""
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="1基本程序:app", host="127.0.0.1", port=8000, reload=True)