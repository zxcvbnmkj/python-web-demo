from fastapi import FastAPI
import gradio as gr

CUSTOM_PATH = "/gradio"

app = FastAPI()


@app.get("/")
def read_main():
    return {"message": "This is your main app"}


io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")

#把gradio挂载到FastAPI中
#启用gradio的登陆系统
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)


# Run this from the terminal as you would normally start a FastAPI app: `uvicorn run:app`
# and navigate to http://localhost:8000/gradio in your browser.

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="1基本集成:app", host="127.0.0.1", port=8000, reload=True)