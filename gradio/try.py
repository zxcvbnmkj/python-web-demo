import gradio as gr



with gr.Blocks() as demo:
    with gr.Column(visible=False) as tips_win:
        tips_Box=gr.Textbox(label="提示框")
        tips_Bt=gr.Button(value="确定")

demo.launch()
